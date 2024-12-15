import pytest
from unittest import mock
from app import db
from app.modules.dataset.models import DataSet, PublicationType
from app.modules.featuremodel.models import FMMetaData, FMMetrics, FeatureModel
from app.modules.featuremodel.repositories import FeatureModelRepository

@pytest.fixture(scope="module")
def test_client(test_client):
    """
    Extends the test_client fixture to add additional specific data for module testing.
    """
    with test_client.application.app_context():
        # Add HERE new elements to the database that you want to exist in the test context.
        # DO NOT FORGET to use db.session.add(<element>) and db.session.commit() to save the data.
        pass

    yield test_client


def test_sample_assertion(test_client):
    """
    Sample test to verify that the test framework and environment are working correctly.
    It does not communicate with the Flask application; it only performs a simple assertion to
    confirm that the tests in this module can be executed.
    """
    greeting = "Hello, World!"
    assert (
        greeting == "Hello, World!"
    ), "The greeting does not coincide with 'Hello, World!'"


@mock.patch('app.modules.featuremodel.repository.FeatureModelRepository.count_feature_models')
def test_count_feature_models(mock_count_feature_models, test_client):
    """
    Test for counting feature models in the database (mocked version).
    """
    # Configuramos el valor de retorno del mock
    mock_count_feature_models.return_value = 5  # Simulamos que hay 5 modelos de características
    
    feature_model_repo = FeatureModelRepository()

    # Pre-condición: Aseguramos que la función mockeada devuelva el valor simulado
    initial_count = feature_model_repo.count_feature_models()
    
    # Verificamos que la función mockeada haya devuelto el valor esperado
    assert initial_count == 5, f"Se esperaba 5, pero se obtuvo {initial_count}"
    
    # Simulamos la creación de un nuevo FeatureModel
    new_feature_model = FeatureModel(data_set_id=1)
    
    # Aquí no se realiza la operación de commit en la base de datos real
    # Simulamos que la operación de commit es exitosa
    with mock.patch.object(db.session, 'commit', return_value=None) as mock_commit:
        db.session.add(new_feature_model)
        db.session.commit()
        
        # Verificamos que la función commit haya sido llamada
        mock_commit.assert_called_once()

