from unittest.mock import MagicMock, patch

import pytest

from app import create_app
from app.modules.dataset.models import DataSet
from app.modules.fakenodo.services import FakenodoService
from app.modules.featuremodel.models import FeatureModel


@pytest.fixture
def fakenodo_service():
    service = FakenodoService()
    service.fakenodo_repository = MagicMock()  # Mock the FakenodoRepository
    service.fakenodos = {}  # Initialize fakenodos as an empty dictionary
    return service


@pytest.fixture
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        }
    )
    with app.app_context():
        yield app


@pytest.fixture
def mock_dataset():
    mock_ds = MagicMock()
    mock_ds.id = 1
    mock_ds.ds_meta_data.title = "Test Dataset"
    mock_ds.ds_meta_data.description = "A test dataset."
    mock_ds.ds_meta_data.authors = []
    mock_ds.ds_meta_data.tags = "tag1, tag2"
    mock_ds.ds_meta_data.publication_type.value = "none"
    return mock_ds


@pytest.fixture
def mock_feature_model():
    mock_fm = MagicMock()
    mock_fm.fm_meta_data.uvl_filename = "test_file.uvl"
    return mock_fm


def test_create_new_fakenodo_invalid_dataset(fakenodo_service):
    invalid_dataset = MagicMock()
    invalid_dataset.ds_meta_data = None
    with pytest.raises(AttributeError):
        fakenodo_service.create_new_fakenodo(invalid_dataset)


def test_get_fakenodo_not_found(fakenodo_service, app):
    with app.app_context():
        with patch("app.modules.fakenodo.models.Fakenodo.query.get", return_value=None):
            with pytest.raises(Exception, match="Fakenodo not found"):
                fakenodo_service.get_fakenodo(1)


def test_get_doi_not_found(fakenodo_service, app):
    with app.app_context():
        with patch("app.modules.fakenodo.models.Fakenodo.query.get", return_value=None):
            with pytest.raises(Exception, match="Fakenodo with ID 1 not found."):
                fakenodo_service.get_doi(1)


def test_get_all_fakenodos_empty(fakenodo_service, app):
    with app.app_context():
        fakenodo_service.fakenodos = {}
        all_fakenodos = fakenodo_service.get_all_fakenodos()
        assert len(all_fakenodos) == 0


def test_upload_file_fakenodo_not_found(
    fakenodo_service, mock_dataset, mock_feature_model, app
):
    with app.app_context():
        with pytest.raises(Exception, match="Deposition not found."):
            fakenodo_service.upload_file(mock_dataset, 1, mock_feature_model)


def test_publish_fakenodo_not_found(fakenodo_service, app):
    with app.app_context():
        with pytest.raises(Exception, match="Fakenodo with ID 1 not found."):
            fakenodo_service.publish_fakenodo(1)


def test_delete_fakenodo_not_found(fakenodo_service, app):
    with app.app_context():
        with pytest.raises(Exception, match="Deposition not found."):
            fakenodo_service.delete_fakenodo(1)


def test_create_new_fakenodo(fakenodo_service, mock_dataset):
    mock_fakenodo = MagicMock()
    mock_fakenodo.id = 1
    mock_fakenodo.meta_data = {
        "title": "Test Dataset",
        "description": "A test dataset.",
        "creators": [],
        "keywords": ["tag1", "tag2", "uvlhub"],
        "license": "CC-BY-4.0",
    }
    fakenodo_service.fakenodo_repository.create_new_fakenodo.return_value = (
        mock_fakenodo
    )

    result = fakenodo_service.create_new_fakenodo(mock_dataset)
    assert "deposition_id" in result
    assert "doi" in result
    assert result["doi"] == None


def test_get_all_fakenodos(fakenodo_service, app):
    with app.app_context():
        fakenodo_service.fakenodos = {
            "1": {"meta_data": {"title": "Test Dataset 1"}, "status": "draft"},
            "2": {"meta_data": {"title": "Test Dataset 2"}, "status": "published"},
        }
        all_fakenodos = fakenodo_service.get_all_fakenodos()
        assert len(all_fakenodos) == 2


def test_delete_fakenodo(fakenodo_service, app):
    with app.app_context():
        fakenodo_service.fakenodos = {
            "1": {"meta_data": {"title": "Test Dataset"}, "status": "draft"}
        }
        response = fakenodo_service.delete_fakenodo("1")
        assert response["message"] == "Deposition deleted successfully."
        assert "1" not in fakenodo_service.fakenodos


def test_get_fakenodo(fakenodo_service, app):
    with app.app_context():
        fakenodo_service.fakenodos = {
            1: {"meta_data": {"title": "Test Dataset"}, "status": "draft"}
        }
        response = fakenodo_service.get_fakenodo(1)
        assert response["meta_data"]["title"] == "Test Dataset"
        assert response["status"] == "draft"


def test_get_doi(fakenodo_service, app):
    with app.app_context():
        fakenodo_service.fakenodos = {
            1: {"meta_data": {"title": "Test Dataset", "doi": None}, "status": "draft"}
        }
        with patch.object(
            fakenodo_service, "_generate_doi", return_value="10.5281/dataset1"
        ):
            doi = fakenodo_service.get_doi(1)
            assert doi == "10.5281/dataset1"
            assert (
                fakenodo_service.fakenodos[1]["meta_data"]["doi"] == "10.5281/dataset1"
            )


def test_publish_fakenodo(fakenodo_service, app):
    fakenodo_service.fakenodos = {
        "1": {"meta_data": {}, "files": [], "status": "draft"}
    }
    response = fakenodo_service.publish_fakenodo("1")
    assert response["status"] == "published"
    assert response["conceptdoi"] == "fakenodo.doi.1"
    assert response["message"] == "Fakenodo published successfully in Fakenodo."
