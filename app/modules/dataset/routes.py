import logging
import os
import re
import shutil
import tempfile
import uuid
from datetime import datetime, timezone
from zipfile import ZipFile

from flask import (abort, jsonify, make_response, redirect, render_template,
                   request, send_from_directory, url_for)
from flask_login import current_user, login_required

from app import db
from app.modules.dataset import dataset_bp
from app.modules.dataset.forms import DataSetForm
from app.modules.dataset.models import DataSet, DSDownloadRecord
from app.modules.dataset.services import (AuthorService, DatasetRatingService,
                                          DataSetService, DOIMappingService,
                                          DSDownloadRecordService,
                                          DSMetaDataService,
                                          DSViewRecordService)
from app.modules.fakenodo.services import FakenodoService
from core.configuration.configuration import USE_FAKENODO

logger = logging.getLogger(__name__)


dataset_service = DataSetService()
author_service = AuthorService()
dsmetadata_service = DSMetaDataService()
fakenodo_service = FakenodoService()
doi_mapping_service = DOIMappingService()
ds_view_record_service = DSViewRecordService()
dataset_rating_service = DatasetRatingService()


@dataset_bp.route("/dataset/upload", methods=["GET", "POST"])
@login_required
def create_dataset():
    form = DataSetForm()
    if request.method == "POST":

        dataset = None

        if not form.validate_on_submit():
            return jsonify({"message": form.errors}), 400

        try:
            logger.info("Creating dataset...")
            dataset = dataset_service.create_from_form(
                form=form, current_user=current_user
            )
            logger.info(f"Created dataset: {dataset}")
            dataset_service.move_feature_models(dataset)
        except Exception as exc:
            logger.exception(f"Exception while creating dataset data locally: {exc}")
            return (
                jsonify({"message": f"Exception while creating dataset: {str(exc)}"}),
                400,
            )

        # send dataset as deposition to Zenodo
        # data = {}
        try:
            # Get the publication DOI (if provided) or fall back to dataset DOI
            publication_doi = (
                form.publication_doi.data if form.publication_doi.data else None
            )

            # Create a new deposition in Fakenodo (or Zenodo) using the dataset
            fakenodo_response_json = fakenodo_service.create_new_fakenodo(
                dataset, publication_doi=publication_doi
            )

            # Log the response for debugging purposes
            logger.info(f"Fakenodo response: {fakenodo_response_json}")

            # Check if the response contains the necessary deposition information (deposition_id and doi)
            if "deposition_id" in fakenodo_response_json:
                deposition_id = fakenodo_response_json.get(
                    "deposition_id"
                )  # Update to the correct key name

                if "doi" in fakenodo_response_json:
                    deposition_doi = fakenodo_response_json.get("doi")
                    dataset_service.update_dsmetadata(
                        dataset.ds_meta_data_id,
                        deposition_id=deposition_id,
                        dataset_doi=deposition_doi,
                    )
                else:
                    dataset_service.update_dsmetadata(
                        dataset.ds_meta_data_id, deposition_id=deposition_id
                    )

                # Return success message with DOI
                return (
                    jsonify(
                        {
                            "status": "success",
                            "message": "Dataset successfully uploaded and DOI generated.",
                            "deposition_doi": deposition_doi,
                        }
                    ),
                    200,
                )
            else:
                # If no deposition ID or DOI is returned, handle the failure case
                logger.error(
                    "Failed to create deposition, missing deposition_id or DOI."
                )
                return (
                    jsonify(
                        {
                            "status": "error",
                            "message": "Deposition creation failed, missing required information.",
                        }
                    ),
                    500,
                )

        except Exception as e:
            # Log and handle errors during the process
            logger.exception(f"Error while creating or processing the deposition: {e}")
            return jsonify({"status": "error", "message": str(e)}), 500

        # Delete temp folder
        file_path = current_user.temp_folder()
        if os.path.exists(file_path) and os.path.isdir(file_path):
            shutil.rmtree(file_path)

        msg = "Everything works!"
        return jsonify({"message": msg}), 200

    return render_template(
        "dataset/upload_dataset.html", form=form, use_fakenodo=USE_FAKENODO
    )


@dataset_bp.route("/dataset/list", methods=["GET", "POST"])
@login_required
def list_dataset():
    return render_template(
        "dataset/list_datasets.html",
        datasets=dataset_service.get_synchronized(current_user.id),
        local_datasets=dataset_service.get_unsynchronized(current_user.id),
    )


@dataset_bp.route("/dataset/file/upload", methods=["POST"])
@login_required
def upload():
    file = request.files["file"]
    temp_folder = current_user.temp_folder()
    publication_doi = request.form.get("publication_doi")

    if not file or not file.filename.endswith(".uvl"):
        return jsonify({"message": "No valid file"}), 400

    if publication_doi:
        # Regex to check the DOI format "10.xxxx"
        if not re.match(r"^10\.\d{4}$", publication_doi):
            return (
                jsonify(
                    {
                        "message": "Invalid DOI format. Please enter a valid DOI like 10.xxxx"
                    }
                ),
                400,
            )

    # create temp folder
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

    file_path = os.path.join(temp_folder, file.filename)

    if os.path.exists(file_path):
        # Generate unique filename (by recursion)
        base_name, extension = os.path.splitext(file.filename)
        i = 1
        while os.path.exists(
            os.path.join(temp_folder, f"{base_name} ({i}){extension}")
        ):
            i += 1
        new_filename = f"{base_name} ({i}){extension}"
        file_path = os.path.join(temp_folder, new_filename)
    else:
        new_filename = file.filename

    try:
        file.save(file_path)
    except Exception as e:
        return jsonify({"message": str(e)}), 500

    return (
        jsonify(
            {
                "message": "UVL uploaded and validated successfully",
                "filename": new_filename,
            }
        ),
        200,
    )


@dataset_bp.route("/dataset/file/delete", methods=["POST"])
def delete():
    data = request.get_json()
    filename = data.get("file")
    temp_folder = current_user.temp_folder()
    filepath = os.path.join(temp_folder, filename)

    if os.path.exists(filepath):
        os.remove(filepath)
        return jsonify({"message": "File deleted successfully"})

    return jsonify({"error": "Error: File not found"})


@dataset_bp.route("/dataset/download/<int:dataset_id>", methods=["GET"])
def download_dataset(dataset_id):
    dataset = dataset_service.get_or_404(dataset_id)

    file_path = f"uploads/user_{dataset.user_id}/dataset_{dataset.id}/"

    temp_dir = tempfile.mkdtemp()
    zip_path = os.path.join(temp_dir, f"dataset_{dataset_id}.zip")

    with ZipFile(zip_path, "w") as zipf:
        for subdir, dirs, files in os.walk(file_path):
            for file in files:
                full_path = os.path.join(subdir, file)

                relative_path = os.path.relpath(full_path, file_path)

                zipf.write(
                    full_path,
                    arcname=os.path.join(
                        os.path.basename(zip_path[:-4]), relative_path
                    ),
                )

    user_cookie = request.cookies.get("download_cookie")
    if not user_cookie:
        user_cookie = str(
            uuid.uuid4()
        )  # Generate a new unique identifier if it does not exist
        # Save the cookie to the user's browser
        resp = make_response(
            send_from_directory(
                temp_dir,
                f"dataset_{dataset_id}.zip",
                as_attachment=True,
                mimetype="application/zip",
            )
        )
        resp.set_cookie("download_cookie", user_cookie)
    else:
        resp = send_from_directory(
            temp_dir,
            f"dataset_{dataset_id}.zip",
            as_attachment=True,
            mimetype="application/zip",
        )

    # Check if the download record already exists for this cookie
    existing_record = DSDownloadRecord.query.filter_by(
        user_id=current_user.id if current_user.is_authenticated else None,
        dataset_id=dataset_id,
        download_cookie=user_cookie,
    ).first()

    if not existing_record:
        # Record the download in your database
        DSDownloadRecordService().create(
            user_id=current_user.id if current_user.is_authenticated else None,
            dataset_id=dataset_id,
            download_date=datetime.now(timezone.utc),
            download_cookie=user_cookie,
        )

    return resp


@dataset_bp.route("/doi/<path:doi>/", methods=["GET"])
def subdomain_index(doi):

    # Check if the DOI is an old DOI
    new_doi = doi_mapping_service.get_new_doi(doi)
    if new_doi:
        # Redirect to the same path with the new DOI
        return redirect(url_for("dataset.subdomain_index", doi=new_doi), code=302)

    # Try to search the dataset by the provided DOI (which should already be the new one)
    ds_meta_data = dsmetadata_service.filter_by_doi(doi)

    if not ds_meta_data:
        abort(404)

    # Get dataset
    dataset = ds_meta_data.data_set

    # Save the cookie to the user's browser
    user_cookie = ds_view_record_service.create_cookie(dataset=dataset)
    resp = make_response(render_template("dataset/view_dataset.html", dataset=dataset))
    resp.set_cookie("view_cookie", user_cookie)

    return resp


@dataset_bp.route("/dataset/unsynchronized/<int:dataset_id>/", methods=["GET"])
@login_required
def get_unsynchronized_dataset(dataset_id):

    # Get dataset
    dataset = dataset_service.get_unsynchronized_dataset(current_user.id, dataset_id)

    if not dataset:
        abort(404)

    return render_template("dataset/view_dataset.html", dataset=dataset)


@dataset_bp.route("/dataset/<int:dataset_id>/", methods=["GET"])
def view_dataset(dataset_id):
    # Obtén el dataset usando el ID
    dataset = dataset_service.get_or_404(dataset_id)

    # Renderiza la plantilla con la información del dataset
    return render_template("dataset/view_dataset.html", dataset=dataset)


@dataset_bp.route("/dataset/toggle_visibility/<int:dataset_id>", methods=["POST"])
def toggle_visibility(dataset_id):
    dataset = DataSet.query.get(dataset_id)
    if dataset:
        # Obtén el nuevo valor de visibilidad desde el cuerpo de la solicitud
        data = request.get_json()
        new_visibility = data.get("publico")

        # Actualiza la visibilidad
        dataset.publico = new_visibility
        db.session.commit()

        return jsonify({"message": "Visibility changed successfully"}), 200
    else:
        return jsonify({"message": "Dataset not found"}), 404


@dataset_bp.route("/dataset/synchronize_datasets", methods=["POST"])
@login_required
def synchronize_datasets():
    try:
        # Obtener los datos enviados desde el frontend
        data = request.get_json()
        print("Datos recibidos:", data)  # Log para verificar los datos recibidos

        # Verificar que datasetId esté presente
        dataset_id = int(data.get("datasetId"))

        if not dataset_id:
            print(
                "Error: No se recibió el datasetId."
            )  # Si el datasetId es None o no está presente
            return jsonify({"message": "El datasetId es requerido."}), 400

        print(
            "datasetId recibido:", dataset_id
        )  # Log para verificar que se recibe el datasetId correctamente

        # Llamar al servicio para sincronizar los datasets con el datasetId
        dataset_service.synchronize_unsynchronized_datasets(current_user.id, dataset_id)

        return (
            jsonify(
                {"success": True, "message": "Datasets sincronizados correctamente."}
            ),
            200,
        )
    except Exception as e:
        print("Error:", e)  # Log para mostrar el error específico
        return jsonify({"message": str(e)}), 400


@dataset_bp.route("/datasets/<int:dataset_id>/rate", methods=["POST"])
@login_required
def rate_dataset(dataset_id):
    data = request.get_json()
    rating_value = data.get("rating")

    if not rating_value:
        return jsonify({"status": "error", "message": "Rating value is required"}), 400

    try:
        # Register or update the rating
        dataset_rating_service.rate_dataset(current_user.id, dataset_id, rating_value)

        # Get updated rating summary
        summary = dataset_rating_service.get_dataset_rating_summary(dataset_id)

        return (
            jsonify(
                {
                    "status": "success",
                    "message": "Rating submitted successfully",
                    "average_rating": summary["average_rating"],
                    "total_ratings": summary["total_ratings"],
                }
            ),
            200,
        )

    except ValueError as e:
        return jsonify({"status": "error", "message": str(e)}), 400
    except Exception as e:
        logger.error(f"Error rating dataset: {e}")
        return jsonify({"status": "error", "message": "An error occurred"}), 500


@dataset_bp.route("/datasets/<int:dataset_id>/ratings", methods=["GET"])
def get_dataset_ratings(dataset_id):
    """Returns the average rating and total number of ratings for a dataset, along with the user's rating."""
    result = dataset_rating_service.get_dataset_rating_summary(dataset_id)
    user_rating = None
    if current_user.is_authenticated:
        user_rating = dataset_rating_service.get_user_rating(
            current_user.id, dataset_id
        )
    return (
        jsonify(
            {
                "average_rating": result["average_rating"],
                "total_ratings": result["total_ratings"],
                "user_rating": user_rating,
            }
        ),
        200,
    )

@dataset_bp.route("/dataset/download_all", methods=["GET"])
def download_all_datasets():
    datasets = dataset_service.get_all()

    temp_dir = tempfile.mkdtemp()
    zip_path = os.path.join(temp_dir, "all_datasets.zip")

    with ZipFile(zip_path, "w") as zipf:
        for dataset in datasets:
            file_path = f"uploads/user_{dataset.user_id}/dataset_{dataset.id}/"
            if os.path.exists(file_path):
                for subdir, dirs, files in os.walk(file_path):
                    for file in files:
                        full_path = os.path.join(subdir, file)
                        relative_path = os.path.relpath(full_path, file_path)
                        zipf.write(full_path, arcname=os.path.join(str(dataset.id), relative_path))

    user_cookie = request.cookies.get("download_cookie")
    if not user_cookie:
        user_cookie = str(uuid.uuid4())

    resp = make_response(
        send_from_directory(
            temp_dir,
            "all_datasets.zip",
            as_attachment=True,
            mimetype="application/zip",
        )
    )
    resp.set_cookie("download_cookie", user_cookie)

    for dataset in datasets:
        existing_record = DSDownloadRecord.query.filter_by(
            dataset_id=dataset.id,
            download_cookie=user_cookie
        ).first()

        if not existing_record:
            DSDownloadRecordService().create(
                user_id=None,
                dataset_id=dataset.id,
                download_date=datetime.now(timezone.utc),
                download_cookie=user_cookie,
            )

    shutil.rmtree(temp_dir)

    return resp