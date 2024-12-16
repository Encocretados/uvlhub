import pytest
from unittest.mock import MagicMock, patch
from app.modules.dashboard.repositories import DashboardRepository
from app.modules.dashboard.services import DashboardService


@pytest.fixture
def dashboard_repository():
    """Fixture para el repositorio del dashboard."""
    return DashboardRepository()


@pytest.fixture
def dashboard_service():
    """Fixture para el servicio del dashboard."""
    return DashboardService()


def test_get_total_datasets(dashboard_repository):
    """Prueba que se obtenga correctamente el total de datasets."""
    dashboard_repository.dataset_repository.count_synchronized_datasets = MagicMock(return_value=10)
    total_datasets = dashboard_repository.get_total_datasets()
    assert total_datasets == 10


def test_get_total_users(dashboard_repository):
    """Prueba que se obtenga correctamente el total de usuarios."""
    dashboard_repository.get_total_users = MagicMock(return_value=5)
    total_users = dashboard_repository.get_total_users()
    assert total_users == 5


def test_get_total_dataset_views(dashboard_repository):
    """Prueba que se obtenga correctamente el total de vistas de datasets."""
    dashboard_repository.get_total_dataset_views = MagicMock(return_value=100)
    total_views = dashboard_repository.get_total_dataset_views()
    assert total_views == 100


def test_get_total_dataset_downloads(dashboard_repository):
    """Prueba que se obtenga correctamente el total de descargas de datasets."""
    dashboard_repository.get_total_dataset_downloads = MagicMock(return_value=20)
    total_downloads = dashboard_repository.get_total_dataset_downloads()
    assert total_downloads == 20


def test_get_total_feature_models(dashboard_repository):
    """Prueba que se obtenga correctamente el total de modelos de características."""
    dashboard_repository.feature_model_repository.count_feature_models = MagicMock(return_value=15)
    total_feature_models = dashboard_repository.get_total_feature_models()
    assert total_feature_models == 15


def test_get_datasets_by_publication_type(dashboard_repository):
    """Prueba que los datasets se agrupen correctamente por PublicationType."""
    dashboard_repository.get_datasets_by_publication_type = MagicMock(return_value={"ARTICLE": 5, "THESIS": 2})
    publication_data = dashboard_repository.get_datasets_by_publication_type()
    assert publication_data == {"ARTICLE": 5, "THESIS": 2}


@patch("app.modules.dashboard.routes.dashboard_service")
def test_dashboard_route(mock_dashboard_service, test_client):
    """Prueba que el endpoint `/dashboard` retorne los datos correctos."""
    mock_dashboard_service.get_dashboard_data.return_value = {
        "total_datasets": 10,
        "total_users": 5,
        "total_views": 100,
        "total_downloads": 20,
        "total_features": 15,
        "publication_type_data": {"ARTICLE": 3, "THESIS": 2},
    }
    mock_dashboard_service.get_total_authors.return_value = 3

    response = test_client.get("/dashboard")
    assert response.status_code == 200
    assert b"Dashboard" in response.data
    assert b"10" in response.data  # Verifica que aparece el total de datasets
    assert b"5" in response.data  # Verifica que aparece el total de usuarios
    assert b"100" in response.data  # Verifica que aparece el total de vistas
    assert b"20" in response.data  # Verifica que aparece el total de descargas
    assert b"15" in response.data  # Verifica que aparece el total de features
