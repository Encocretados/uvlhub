import hashlib
import logging
import os

from dotenv import load_dotenv
from flask_login import current_user

from app.modules.dataset.models import DataSet, DSMetaData
from app.modules.fakenodo.models import Fakenodo
from app.modules.fakenodo.repositories import FakenodoRepository
from app.modules.featuremodel.models import FeatureModel
from core.configuration.configuration import uploads_folder_name
from core.services.BaseService import BaseService

logger = logging.getLogger(__name__)

load_dotenv()


class FakenodoService(BaseService):
    def __init__(self):
        self.fakenodo_repository = FakenodoRepository()
        self.fakenodos = {}  # Initialize depositions as an empty dictionary

    def create_new_fakenodo(
        self, dataset: DataSet, publication_doi: str = None
    ) -> dict:
        """
        Create a new fakenodo in Fakenodo.

        Args:
            dataset (DSMetaData): The dataset containing the required metadata.

        Returns:
            dict: A JSON object with the details of the created fakenodo.
        """
        fakenodo_id = dataset.id

        # If publication DOI is provided and valid, use it; otherwise, generate a DOI
        if publication_doi:
            fake_doi = f"{publication_doi}/dataset{fakenodo_id}"
        else:
            fake_doi = None

        metadata = self._build_metadata(dataset)

        try:
            fakenodo = self.fakenodo_repository.create_new_fakenodo(meta_data=metadata)
            return self._build_response(
                fakenodo,
                metadata,
                "Fakenodo successfully created in Fakenodo",
                fake_doi,
            )
        except Exception as error:
            raise Exception(
                f"Failed to create fakenodo in Fakenodo with error: {str(error)}"
            )

    def upload_file(
        self, dataset: DataSet, fakenodo_id: int, feature_model: FeatureModel, user=None
    ):
        """
        Upload a file to a fakenodo in Fakenodo.

        Args:
            fakenodo_id (int): The unique identifier of the fakenodo in Fakenodo.
            feature_model (FeatureModel): An object representing the feature model.
            user (User): An object representing the file owner.

        Returns:
            dict: A JSON object containing the details of the uploaded file.
        """
        if fakenodo_id not in self.fakenodos:
            raise Exception("Deposition not found.")

        file_name = feature_model.fm_meta_data.uvl_filename
        user_id = current_user.id if user is None else user.id
        file_path = os.path.join(
            uploads_folder_name(),
            f"user_{str(user_id)}",
            f"dataset_{dataset.id}/",
            file_name,
        )

        # Simulate saving the file in local storage
        if not os.path.exists(file_path):
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, "w") as f:
                f.write("Simulated file content.")

        # Add the file to the deposition's local record
        self.fakenodos[fakenodo_id]["files"].append(file_name)

        file_metadata = {
            "file_name": file_name,
            "file_size": os.path.getsize(file_path),
            "file_url": f"/uploads/user_{current_user.id}/dataset_{dataset.id}/{file_name}",
        }

        return {
            "message": f"File {file_name} uploaded successfully.",
            "file_metadata": file_metadata,
        }

    def publish_fakenodo(self, fakenodo_id: str) -> dict:
        """
        Publish a fakenodo in Fakenodo.

        Args:
            fakenodo_id (str): The unique identifier of the fakenodo in Fakenodo.

        Returns:
            dict: A JSON object containing the details of the published fakenodo.
        """
        # Assuming depositions are stored in a dictionary or similar structure
        fakenodo = self.fakenodos.get(fakenodo_id)

        if not fakenodo:
            # Raise an error if the fakenodo with the provided ID is not found
            raise Exception(f"Fakenodo with ID {fakenodo_id} not found.")

        try:
            # Simulate generating a DOI for the fakenodo
            fakenodo["doi"] = f"fakenodo.doi.{fakenodo_id}"
            fakenodo["status"] = "published"  # Mark the fakenodo as published

            # Update the fakenodo in your storage (e.g., database or dictionary)
            self.fakenodos[fakenodo_id] = fakenodo

            # Return a success response with the fakenodo details
            response = {
                "id": fakenodo_id,
                "status": "published",
                "conceptdoi": fakenodo["doi"],  # Use the generated DOI here
                "message": "Fakenodo published successfully in Fakenodo.",
            }
            return response

        except Exception as error:
            # Handle any errors that occur during the process and raise a new exception
            raise Exception(f"Failed to publish fakenodo with error: {str(error)}")

    def get_fakenodo(self, fakenodo_id: int) -> dict:
        """
        Retrieve details of a fakenodo from Fakenodo.

        Args:
            fakenodo_id (int): The unique identifier of the fakenodo in Fakenodo.

        Returns:
            dict: A JSON object containing the details of the specified fakenodo.
        """
        fakenodo = self.fakenodos.get(fakenodo_id)
        if not fakenodo:
            raise Exception("Fakenodo not found")

        return fakenodo

    def get_doi(self, fakenodo_id: int) -> str:
        """
        Retrieve the DOI (Digital Object Identifier) of a fakenodo from Fakenodo.

        Args:
            fakenodo_id (int): The unique identifier of the fakenodo in Fakenodo.

        Returns:
            str: The DOI associated with the specified fakenodo.
        """
        fakenodo = self.fakenodos.get(fakenodo_id)
        if not fakenodo:
            raise Exception(f"Fakenodo with ID {fakenodo_id} not found.")

        if "doi" not in fakenodo["meta_data"] or fakenodo["meta_data"]["doi"] == None:
            generated_doi = self._generate_doi(fakenodo_id)
            fakenodo["meta_data"]["doi"] = generated_doi
        return fakenodo["meta_data"]["doi"]

    def _build_metadata(self, dataset: DSMetaData) -> dict:
        """
        Build metadata JSON from DSMetaData.

        Args:
            dataset (DSMetaData): The dataset metadata.

        Returns:
            dict: The metadata JSON.
        """
        return {
            "title": dataset.ds_meta_data.title,
            "upload_type": (
                "dataset"
                if dataset.ds_meta_data.publication_type.value == "none"
                else "publication"
            ),
            "publication_type": (
                dataset.ds_meta_data.publication_type.value
                if dataset.ds_meta_data.publication_type.value != "none"
                else None
            ),
            "description": dataset.ds_meta_data.description,
            "creators": [
                {
                    "name": author.name,
                    **(
                        {"affiliation": author.affiliation}
                        if author.affiliation
                        else {}
                    ),
                    **({"orcid": author.orcid} if author.orcid else {}),
                }
                for author in dataset.ds_meta_data.authors
            ],
            "keywords": (
                ["uvlhub"]
                if not dataset.ds_meta_data.tags
                else dataset.ds_meta_data.tags.split(", ") + ["uvlhub"]
            ),
            "access_right": "open",
            "license": "CC-BY-4.0",
        }

    def _build_response(self, fakenodo, meta_data, message, doi) -> dict:
        """
        Build a response JSON.

        Args:
            fakenodo (Fakenodo): The fakenodo object.
            meta_data (dict): The metadata JSON.
            message (str): The response message.

        Returns:
            dict: The response JSON.
        """
        return {
            "deposition_id": fakenodo.id,  # ID from the repository
            "doi": doi,
            "meta_data": meta_data,
            "message": message,
        }

    def _calculate_checksum(self, file_path: str) -> str:
        """
        Calculate the checksum of a file.

        Args:
            file_path (str): The path to the file.

        Returns:
            str: The checksum of the file.
        """
        try:
            with open(file_path, "rb") as file:
                file_content = file.read()
                return hashlib.sha256(
                    file_content
                ).hexdigest()  # Use SHA-256 instead of MD5
        except FileNotFoundError:
            raise Exception(f"File {file_path} not found for checksum calculation")
        except Exception as e:
            raise Exception(
                f"Error calculating checksum for file {file_path}: {str(e)}"
            )

    def _generate_doi(self, deposition_id):
        """Generate a fake DOI based on the deposition ID."""
        return f"10.5281/dataset{deposition_id}"

    def get_all_fakenodos(self) -> dict:
        """
        Get all depositions from Fakenodo.
        """
        return self.fakenodos

    def delete_fakenodo(self, deposition_id: str) -> dict:
        """
        Simulate deleting a deposition from Fakenodo.
        """
        if deposition_id not in self.fakenodos:
            raise Exception("Deposition not found.")

        # Simulate deletion
        del self.fakenodos[deposition_id]

        return {"message": "Deposition deleted successfully."}
