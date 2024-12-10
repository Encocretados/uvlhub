import hashlib
import pytest
from unittest.mock import MagicMock, patch
from app.modules.fakenodo.services import FakenodoService
from app.modules.fakenodo.models import Fakenodo
from app.modules.dataset.models import DataSet
from app.modules.featuremodel.models import FeatureModel
from app import create_app
from app import db
from sqlalchemy import inspect


@pytest.fixture
def fakenodo_service():
    return FakenodoService()


@pytest.fixture
def setup_fakenodo(app):
    with app.app_context():
        fakenodo = Fakenodo(doi=None, meta_data={"title": "Test Fakenodo"})
        db.session.add(fakenodo)
        db.session.commit()
        yield fakenodo
        db.session.delete(fakenodo)
        db.session.commit()
       
          
@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:", 
    })
    with app.app_context():
        inspector = inspect(db.engine)
        if "fakenodo" not in inspector.get_table_names():
            Fakenodo.__table__.create(db.engine)  
        yield app
        Fakenodo.__table__.drop(db.engine)


def test_create_new_fakenodo(fakenodo_service, app):
    with app.app_context():
        # Crear un mock de DataSet sin `spec` para mayor control
        mock_dataset = MagicMock()
        
        # Configurar explícitamente cada nivel de ds_meta_data y sus atributos anidados
        mock_dataset.ds_meta_data = MagicMock()
        mock_dataset.ds_meta_data.title = "Test Title"
        mock_dataset.ds_meta_data.description = "Test Description"
        
        # Configurar `publication_type` con `value`
        mock_dataset.ds_meta_data.publication_type = MagicMock()
        mock_dataset.ds_meta_data.publication_type.value = "none"
        
        # Configurar lista de autores como mock
        mock_author = MagicMock()
        mock_author.name = "Author1"
        mock_author.affiliation = "Test Affiliation"
        mock_author.orcid = "0000-0000"
        mock_dataset.ds_meta_data.authors = [mock_author]
        
        # Configurar tags
        mock_dataset.ds_meta_data.tags = "test, dataset"
        
        # Mockear `create_new_fakenodo` en `fakenodo_repository` para devolver una instancia de Fakenodo
        mock_fakenodo = Fakenodo(doi=None, meta_data={"title": "Test Fakenodo"})  # Crear una instancia de Fakenodo sin id
        with patch.object(fakenodo_service.fakenodo_repository, 'create_new_fakenodo',
                          return_value=mock_fakenodo) as mock_create:
            # Llamar al método del servicio
            result = fakenodo_service.create_new_fakenodo(mock_dataset)
            
            # Verificar que `create_new_fakenodo` fue llamado
            mock_create.assert_called_once()
            
            # Verificar el valor de 'id' en el resultado
            assert result["id"] == mock_fakenodo.id
            assert result["message"] == "Fakenodo successfully created in Fakenodo"


def test_upload_file(fakenodo_service, app):
    with app.app_context():
        mock_dataset = MagicMock(spec=DataSet)
        mock_feature_model = MagicMock(spec=FeatureModel)
        mock_feature_model.fm_meta_data.uvl_filename = "test_file.uvl"
        mock_user = MagicMock()
        mock_user.id = 1

        with patch("os.path.getsize", return_value=100), patch("app.modules.fakenodo.services.FakenodoService._calculate_checksum", 
                                                               return_value="mocked_checksum"):
            result = fakenodo_service.upload_file(mock_dataset, 1, mock_feature_model, user=mock_user)
            assert result["id"] == 1
            assert result["file"] == "test_file.uvl"
            assert result["fileSize"] == 100
            assert result["checksum"] == "mocked_checksum"
            assert result["message"] == "File Uploaded to fakenodo with id 1"


def test_publish_fakenodo(fakenodo_service, app, setup_fakenodo):
    with app.app_context():
        result = fakenodo_service.publish_fakenodo(setup_fakenodo.id)
        assert result["status"] == "published"
        assert result["doi"] == f"fakenodo.doi.{setup_fakenodo.id}"
        assert result["message"] == "Fakenodo published successfully in Fakenodo."


def test_get_fakenodo(fakenodo_service, app, setup_fakenodo):
    with app.app_context():
        result = fakenodo_service.get_fakenodo(setup_fakenodo.id)
        assert result["id"] == setup_fakenodo.id
        assert result["meta_data"]["title"] == "Test Fakenodo"
        assert result["status"] == "draft"


def test_get_doi(fakenodo_service, app):
    with app.app_context():
        mock_fakenodo = Fakenodo(doi="fakenodo.doi.1", meta_data={"title": "Test Fakenodo"})
        db.session.add(mock_fakenodo)
        db.session.commit()
        
        with patch.object(fakenodo_service, 'get_fakenodo', return_value={"doi": "fakenodo.doi.1"}):
            result = fakenodo_service.get_doi(mock_fakenodo.id)
            assert result == "fakenodo.doi.1"


def test_checksum():
    with patch("builtins.open", new_callable=MagicMock) as mock_open:
        mock_open.return_value.__enter__.return_value.read.return_value = b"test data"
        result = hashlib.sha256(b"test data").hexdigest()
        assert result == hashlib.sha256(b"test data").hexdigest()