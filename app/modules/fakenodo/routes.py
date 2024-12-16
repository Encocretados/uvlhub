from flask import jsonify, request
from flask_login import login_required

from app.modules.dataset.models import DataSet
from app.modules.fakenodo import fakenodo_bp
from app.modules.fakenodo.services import FakenodoService
from app.modules.featuremodel.models import FeatureModel

base_url = "/fakenodo/api"


# Test connection (GET)
@fakenodo_bp.route(base_url + "/test_connection", methods=["GET"])
@login_required
def test_connection_fakenodo():
    service = FakenodoService()
    if service.test_connection():
        response = {"status": "success", "message": "Connected to FakenodoAPI"}
    else:
        response = {"status": "error", "message": "Connection failed"}
    return jsonify(response)


# Create a new fakenodo (POST)
@fakenodo_bp.route(base_url + "/fakenodos", methods=["POST"])
@login_required
def create_fakenodo():
    try:
        dataset_id = request.json.get("dataset_id")
        dataset = DataSet.query.get(dataset_id)

        if not dataset:
            return jsonify({"status": "error", "message": "Dataset not found."}), 404

        service = FakenodoService()
        fakenodo_data = service.create_new_fakenodo(dataset)

        return (
            jsonify(
                {
                    "status": "success",
                    "message": "Fakenodo created successfully.",
                    "fakenodo": fakenodo_data,
                }
            ),
            201,
        )

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


# Upload file to a fakenodo (POST)
@fakenodo_bp.route(base_url + "/<fakenodo_id>/files", methods=["POST"])
@login_required
def upload_file(fakenodo_id):
    try:
        # Get the dataset_id and feature_model_id from the form data
        dataset_id = request.form.get("dataset_id")
        feature_model_id = request.form.get("feature_model_id")

        # Fetch the Dataset and FeatureModel objects from the database
        dataset = DataSet.query.get(dataset_id)
        feature_model = FeatureModel.query.get(feature_model_id)

        # Check if dataset or feature model is not found
        if not dataset or not feature_model:
            return (
                jsonify(
                    {"status": "error", "message": "Dataset or FeatureModel not found."}
                ),
                404,
            )

        # Create an instance of the FakenodoService
        service = FakenodoService()

        # Call the upload_file method from the service to simulate file upload
        response = service.upload_file(dataset, fakenodo_id, feature_model)

        # Return a success response with the file metadata
        return (
            jsonify(
                {
                    "status": "success",
                    "message": response["message"],
                    "file_metadata": response.get("file_metadata", {}),
                }
            ),
            201,
        )  # HTTP Status Code 201 for successful resource creation

    except Exception as e:
        # In case of an error, return a generic error message with exception details
        return jsonify({"status": "error", "message": str(e)}), 500


# Publish a fakenodo (PUT)
@fakenodo_bp.route(base_url + "/<fakenodo_id>/publish", methods=["PUT"])
@login_required
def publish_fakenodo(fakenodo_id):
    try:
        service = FakenodoService()
        message = service.publish_fakenodo(fakenodo_id)

        return jsonify({"status": "success", "message": message["message"]}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


# Get a fakenodo's details (GET)
@fakenodo_bp.route(base_url + "/<fakenodo_id>", methods=["GET"])
@login_required
def get_fakenodo(fakenodo_id):
    try:
        service = FakenodoService()
        fakenodo = service.get_fakenodo(fakenodo_id)

        return jsonify({"status": "success", "fakenodo": fakenodo}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


# Get the DOI of a fakenodo (GET)
@fakenodo_bp.route(base_url + "/<fakenodo_id>/doi", methods=["GET"])
@login_required
def get_doi(fakenodo_id):
    try:
        service = FakenodoService()
        doi = service.get_doi(fakenodo_id)

        return jsonify({"status": "success", "doi": doi}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


# Get all fakenodos (GET)
@fakenodo_bp.route(base_url + "/fakenodos", methods=["GET"])
@login_required
def get_all_fakenodos():
    try:
        service = FakenodoService()
        fakenodos = service.get_all_fakenodos()

        return jsonify({"status": "success", "fakenodos": fakenodos}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


# Delete a fakenodo (DELETE)
@fakenodo_bp.route(base_url + "/<fakenodo_id>", methods=["DELETE"])
@login_required
def delete_fakenodo(fakenodo_id):
    try:
        service = FakenodoService()
        message = service.delete_fakenodo(fakenodo_id)

        return jsonify({"status": "success", "message": message["message"]}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
