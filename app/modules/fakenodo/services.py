import logging
import hashlib
import os

from dotenv import load_dotenv
from app.modules.fakenodo.repositories import FakenodoRepository
from app.modules.fakenodo.models import Fakenodo
from app.modules.dataset.models import DataSet, DSMetaData
from app.modules.featuremodel.models import FeatureModel

from core.configuration.configuration import uploads_folder_name
from core.services.BaseService import BaseService
from flask_login import current_user

logger = logging.getLogger(__name__)

load_dotenv()


class FakenodoService(BaseService):
    def __init__(self):
        self.fakenodo_repository = FakenodoRepository()

    def create_new_fakenodo(self, ds_meta_data: DSMetaData) -> dict:
        """
        Create a new fakenodo in Fakenodo.

        Args:
            ds_meta_data (DSMetaData): The dataset containing the required metadata.

        Returns:
            dict: A JSON object with the details of the created fakenodo.
        """
        logger.info("Dataset sending to Fakenodo")
        logger.info(f"Publication type: {ds_meta_data.publication_type.value}")

        metadata = self._build_metadata(ds_meta_data)

        try:
            fakenodo = self.fakenodo_repository.create_new_fakenodo(meta_data=metadata)
            return self._build_response(fakenodo, metadata, "Fakenodo successfully created in Fakenodo")
        except Exception as error:
            raise Exception(f"Failed to create fakenodo in Fakenodo with error: {str(error)}")

    def upload_file(self, dataset: DataSet, fakenodo_id: int, feature_model: FeatureModel, user=None):
        """
        Upload a file to a fakenodo in Fakenodo.

        Args:
            fakenodo_id (int): The unique identifier of the fakenodo in Fakenodo.
            feature_model (FeatureModel): An object representing the feature model.
            user (User): An object representing the file owner.

        Returns:
            dict: A JSON object containing the details of the uploaded file.
        """
        uvl_filename = feature_model.fm_meta_data.uvl_filename
        user_id = current_user.id if user is None else user.id
        file_path = os.path.join(uploads_folder_name(), f"user_{str(user_id)}", f"dataset_{dataset.id}/", uvl_filename)

        request = {
            "id": fakenodo_id,
            "file": uvl_filename,
            "fileSize": os.path.getsize(file_path),
            "checksum": self._calculate_checksum(file_path),
            "message": f"File Uploaded to fakenodo with id {fakenodo_id}"
        }

        return request

    def publish_fakenodo(self, fakenodo_id: int) -> dict:
        """
        Publish a fakenodo in Fakenodo.

        Args:
            fakenodo_id (int): The unique identifier of the fakenodo in Fakenodo.

        Returns:
            dict: A JSON object containing the details of the published fakenodo.
        """
        fakenodo = Fakenodo.query.get(fakenodo_id)
        if not fakenodo:
            raise Exception("Error 404: Fakenodo not found")

        try:
            fakenodo.doi = f"fakenodo.doi.{fakenodo_id}"
            fakenodo.status = "published"
            self.fakenodo_repository.update(fakenodo)
            return self._build_response(fakenodo, fakenodo.meta_data, "Fakenodo published successfully in Fakenodo")
        except Exception as error:
            raise Exception(f"Failed to publish fakenodo with errors: {str(error)}")

    def get_fakenodo(self, fakenodo_id: int) -> dict:
        """
        Retrieve details of a fakenodo from Fakenodo.

        Args:
            fakenodo_id (int): The unique identifier of the fakenodo in Fakenodo.

        Returns:
            dict: A JSON object containing the details of the specified fakenodo.
        """
        fakenodo = Fakenodo.query.get(fakenodo_id)
        if not fakenodo:
            raise Exception("Fakenodo not found")

        return self._build_response(fakenodo, fakenodo.meta_data, "Fakenodo successfully retrieved from Fakenodo")

    def get_doi(self, fakenodo_id: int) -> str:
        """
        Retrieve the DOI (Digital Object Identifier) of a fakenodo from Fakenodo.

        Args:
            fakenodo_id (int): The unique identifier of the fakenodo in Fakenodo.

        Returns:
            str: The DOI associated with the specified fakenodo.
        """
        fakenodo = Fakenodo.query.get(fakenodo_id)
        if not fakenodo:
            raise Exception(f"Fakenodo with ID {fakenodo_id} not found.")

        # Check if DOI is already assigned, otherwise generate one
        if "doi" not in fakenodo.meta_data:
            # Simulate DOI generation (format: 10.xxxx/yyyyyy)
            generated_doi = self._generate_doi(fakenodo_id)
            fakenodo.meta_data["doi"] = generated_doi
        return fakenodo.meta_data["doi"]

    def _build_metadata(self, ds_meta_data: DSMetaData) -> dict:
        """
        Build metadata JSON from DSMetaData.

        Args:
            ds_meta_data (DSMetaData): The dataset metadata.

        Returns:
            dict: The metadata JSON.
        """
        return {
            "title": ds_meta_data.title,
            "upload_type": "dataset" if ds_meta_data.publication_type.value == "none" else "publication",
            "publication_type": (
                ds_meta_data.publication_type.value
                if ds_meta_data.publication_type.value != "none"
                else None
            ),
            "description": ds_meta_data.description,
            "creators": [
                {
                    "name": author.name,
                    **({"affiliation": author.affiliation} if author.affiliation else {}),
                    **({"orcid": author.orcid} if author.orcid else {}),
                }
                for author in ds_meta_data.authors
            ],
            "keywords": (
                ["uvlhub"] if not ds_meta_data.tags else ds_meta_data.tags.split(", ") + ["uvlhub"]
            ),
            "access_right": "open",
            "license": "CC-BY-4.0",
        }

    def _build_response(self, fakenodo, meta_data, message) -> dict:
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
            "id": fakenodo.id,
            "meta_data": meta_data,
            "message": message
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
                return hashlib.md5(file_content).hexdigest()
        except FileNotFoundError:
            raise Exception(f"File {file_path} not found for checksum calculation")
        except Exception as e:
            raise Exception(f"Error calculating checksum for file {file_path}: {str(e)}")

    def _generate_doi(self, fakenodo_id: int) -> str:
        """
        Generate a DOI for a fakenodo.

        Args:
            fakenodo_id (int): The unique identifier of the fakenodo.

        Returns:
            str: The generated DOI.
        """
        return f"10.5281/{fakenodo_id}"