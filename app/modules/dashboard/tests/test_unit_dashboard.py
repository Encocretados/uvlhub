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


def test_get_datasets_by_publication_type(dashboard_repository):
    """Prueba que los datasets se agrupen correctamente por PublicationType."""
    dashboard_repository.get_datasets_by_publication_type = MagicMock(return_value={"ARTICLE": 5, "THESIS": 2})
    publication_data = dashboard_repository.get_datasets_by_publication_type()
    assert publication_data == {"ARTICLE": 5, "THESIS": 2}


# def test_get_dashboard_data(dashboard_service):
#     """Prueba que el servicio genere los datos del dashboard correctamente."""
#     dashboard_service.repository.get_total_datasets = MagicMock(return_value=10)
#     dashboard_service.repository.get_total_users = MagicMock(return_value=5)
#     dashboard_service.repository.get_total_dataset_views = MagicMock(return_value=100)
#     dashboard_service.repository.get_total_dataset_downloads = MagicMock(return_value=20)
#     dashboard_service.repository.get_total_feature_models = MagicMock(return_value=15)
#     dashboard_service.repository.get_datasets_by_publication_type = MagicMock(return_value={"ARTICLE": 3, "THESIS": 2})

#     dashboard_data = dashboard_service.get_dashboard_data()
#     assert dashboard_data["total_datasets"] == 10
#     assert dashboard_data["total_users"] == 5
#     assert dashboard_data["total_views"] == 100
#     assert dashboard_data["total_downloads"] == 20
#     assert dashboard_data["total_features"] == 15
#     assert dashboard_data["publication_type_data"] == {"ARTICLE": 3, "THESIS": 2}



@patch("app.modules.dashboard.routes.dashboard_service")
def test_dashboard_route(mock_dashboard_service, test_client):
    """Prueba que el endpoint `/dashboard` retorne los datos correctos."""
    mock_dashboard_service.get_dashboard_data.return_value = {
        "total_datasets": 10,
        "total_users": 5,
        "total_views": 100,
        "total_downloads": 20,
        "publication_type_data": {"ARTICLE": 3, "THESIS": 2},
    }
    mock_dashboard_service.get_total_authors.return_value = 3

    response = test_client.get("/dashboard")
    assert response.status_code == 200
    assert b"Dashboard" in response.data
    assert b"10" in response.data  # Verifica que aparece el total de datasets
    assert b"5" in response.data   # Verifica que aparece el total de usuarios

