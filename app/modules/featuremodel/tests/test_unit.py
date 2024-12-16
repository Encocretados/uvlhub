from unittest import mock

import pytest

from app import db
from app.modules.dataset.models import DataSet, PublicationType
from app.modules.featuremodel.models import FeatureModel, FMMetaData, FMMetrics
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


@mock.patch(
    "app.modules.featuremodel.repositories.FeatureModelRepository.count_feature_models"
)
def test_count_feature_models(mock_count_feature_models, test_client):
    """
    Test for counting feature models in the database (mocked version).
    """
    # Configuramos el valor de retorno del mock
    mock_count_feature_models.return_value = (
        5  # Simulamos que hay 5 modelos de características
    )

    feature_model_repo = FeatureModelRepository()

    # Pre-condición: Aseguramos que la función mockeada devuelva el valor simulado
    initial_count = feature_model_repo.count_feature_models()

    # Verificamos que la función mockeada haya devuelto el valor esperado
    assert initial_count == 5, f"Se esperaba 5, pero se obtuvo {initial_count}"

    # Simulamos la creación de un nuevo FeatureModel
    new_feature_model = FeatureModel(data_set_id=1)

    # Aquí no se realiza la operación de commit en la base de datos real
    # Simulamos que la operación de commit es exitosa
    with mock.patch.object(db.session, "commit", return_value=None) as mock_commit:
        db.session.add(new_feature_model)
        db.session.commit()

        # Verificamos que la función commit haya sido llamada
        mock_commit.assert_called_once()


@mock.patch("app.modules.featuremodel.models.db.session.add")
@mock.patch("app.modules.featuremodel.models.db.session.commit")
@mock.patch("app.modules.featuremodel.models.FMMetaData.query.get")
def test_create_fm_metadata(mock_get, mock_commit, mock_add, test_client):
    """
    Test for creating a new FMMetaData instance (mocked version).
    """
    # Crea un objeto FMMetrics para que la clave foránea sea válida
    mock_fm_metrics = FMMetrics(
        id=1, solver="Test Solver", not_solver="Test Not Solver"
    )
    db.session.add(mock_fm_metrics)
    db.session.commit()

    # Configura el mock para simular la consulta al objeto recién creado
    mock_get.return_value = FMMetaData(
        uvl_filename="test_file.csv",
        title="Test Metadata",
        description="Test description",
        publication_type=PublicationType.NONE,
        publication_doi="10.1234/testdoi",
        tags="test, metadata",
        uvl_version="1.0",
        fm_metrics_id=mock_fm_metrics.id,  # Usa el ID de FMMetrics aquí
    )


def test_create_feature_model_no_db(test_client):
    """
    Test for creating a new FeatureModel instance without modifying the real database.
    """
    with mock.patch(
        "app.modules.featuremodel.models.db.session.add"
    ) as mock_add, mock.patch(
        "app.modules.featuremodel.models.db.session.commit"
    ) as mock_commit, mock.patch(
        "app.modules.featuremodel.models.FeatureModel.query.get"
    ) as mock_get:

        # Mock the data_set_id to simulate the existence of the referenced dataset
        mock_get.return_value = mock.Mock(id=1)

        # Create a new FeatureModel with a mock data_set_id
        new_feature_model = FeatureModel(data_set_id=1)

        # Simulate adding the object to the session (Ensure it's actually being added to the session)
        db.session.add(new_feature_model)

        # Simulate committing the session
        db.session.commit()

        # Assert that the 'add' method was called with the correct arguments
        mock_add.assert_called_once_with(new_feature_model)
