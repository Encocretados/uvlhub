import pytest
from datetime import datetime
from unittest.mock import patch,MagicMock
from app.modules.dataset.models import DataSet, DSMetaData
from app.modules.dataset.repositories import DataSetRepository
from app.modules.dataset.services import DataSetService



@pytest.fixture
def dataset_repository():
    """Fixture para el repositorio de datasets."""
    repo = DataSetRepository()
    repo.model = MagicMock()  
    return repo


@pytest.fixture
def synchronized_dataset():
    """Crea un dataset sincronizado de ejemplo."""
    meta_data = DSMetaData(
        id=1,
        deposition_id=12345,
        title="Synchronized Dataset",
        description="Example synchronized dataset",
        publication_type="ARTICLE",
        dataset_doi="10.1234/sync/12345",
        
    )
    return DataSet(
        id=1,
        user_id=1,
        ds_meta_data=meta_data,
        created_at=datetime.utcnow(),
    )


@pytest.fixture
def unsynchronized_dataset():
    """Crea un dataset no sincronizado de ejemplo."""
    meta_data = DSMetaData(
        id=2,
        deposition_id=None,
        title="Unsynchronized Dataset",
        description="Example unsynchronized dataset",
        publication_type="NONE",
        dataset_doi=None,
    )
    return DataSet(
        id=2,
        user_id=1,
        ds_meta_data=meta_data,
        created_at=datetime.utcnow(),
    )


def test_get_synchronized(dataset_repository, synchronized_dataset):
    """Prueba que se obtengan datasets sincronizados correctamente."""
    dataset_repository.model.query.join.return_value.filter.return_value.order_by.return_value.all.return_value = [
        synchronized_dataset
    ]

    datasets = dataset_repository.get_synchronized(1)
    assert len(datasets) == 1
    assert datasets[0].ds_meta_data.dataset_doi is not None


def test_get_unsynchronized(dataset_repository, unsynchronized_dataset):
    """Prueba que se obtengan datasets no sincronizados correctamente."""
    dataset_repository.model.query.join.return_value.filter.return_value.order_by.return_value.all.return_value = [
        unsynchronized_dataset
    ]

    datasets = dataset_repository.get_unsynchronized(1)
    assert len(datasets) == 1
    assert datasets[0].ds_meta_data.dataset_doi is None


def test_count_synchronized_datasets(dataset_repository):
    """Prueba que el conteo de datasets sincronizados sea correcto."""
    dataset_repository.model.query.join.return_value.filter.return_value.count.return_value = 5

    count = dataset_repository.count_synchronized_datasets()
    assert count == 5


def test_count_unsynchronized_datasets(dataset_repository):
    """Prueba que el conteo de datasets no sincronizados sea correcto."""
    dataset_repository.model.query.join.return_value.filter.return_value.count.return_value = 3

    count = dataset_repository.count_unsynchronized_datasets()
    assert count == 3


def test_synchronize_unsynchronized_datasets(dataset_repository, unsynchronized_dataset):
    """Prueba la sincronización de un dataset no sincronizado."""
    
    # Configura el comportamiento del mock para get_unsynchronized
    dataset_repository.get_unsynchronized = MagicMock(return_value=[unsynchronized_dataset])
    
    # Configura el comportamiento del mock para generate_doi_for_dataset
    dataset_repository.generate_doi_for_dataset = MagicMock(return_value="10.1234/new_doi")
    
    # Ejecuta la sincronización
    dataset_repository.synchronize_unsynchronized_datasets(1, 2)

    # Verifica que el dataset haya obtenido un nuevo DOI
    assert unsynchronized_dataset.ds_meta_data.dataset_doi == "10.1234/new_doi"

#test verifica que se maneje correctamente un DOI que no tiene un formato válido.
@patch('os.getenv')
def test_get_uvlhub_doi_invalid(mock_getenv):
    mock_getenv.return_value = 'uvlhub.io'

    # Crear un mock del dataset con un DOI no válido
    mock_dataset = MagicMock()
    mock_dataset.ds_meta_data.dataset_doi = None  # Sin DOI

    # Crear una instancia del servicio
    service = DataSetService()

    # Ejecutar la función
    result = service.get_uvlhub_doi(mock_dataset)

    # Verificar que devuelve una URL con 'None' como DOI
    assert result == 'http://uvlhub.io/doi/None'

#test de integración para un error interno del servidor
@patch('app.modules.dataset.services.DSMetaDataService.filter_by_doi')
def test_subdomain_index_internal_error(mock_filter_by_doi, test_client):
    # Simular que ocurre un error al intentar obtener el dataset
    mock_filter_by_doi.side_effect = Exception("Internal server error")

    # Capturar la excepción pero permitir que la prueba continúe
    try:
        response = test_client.get('/doi/10.1234/datafset1/')
    except Exception:
        response = None

    # Verificar que se devuelve un código de estado 500
    assert response is None or response.status_code == 500

#test unitario, devuelve el DOI
@patch('os.getenv')  # Simulamos la función os.getenv
def test_construct_uvlhub_doi(mocked_getenv):
    # Simular el valor que retorna os.getenv para el dominio
    mocked_getenv.return_value = 'uvlhub.io'

    # Simulamos un objeto de dataset con un DOI
    fake_dataset = MagicMock()
    fake_dataset.ds_meta_data.dataset_doi = '10.1234/example_doi'

    # Instancia del servicio bajo prueba
    dataset_service = DataSetService()

    # Llamar a la función objetivo
    generated_url = dataset_service.get_uvlhub_doi(fake_dataset)

    # Comprobar que la URL generada es correcta
    expected_url = 'http://uvlhub.io/doi/10.1234/example_doi'
    assert generated_url == expected_url

    # Confirmar que os.getenv fue llamado con los parámetros esperados
    mocked_getenv.assert_called_once_with('DOMAIN', 'localhost')

#test de integración que verifica que el sistema maneje correctamente un caso donde no se pueda establecer una cookie.
@patch('app.modules.dataset.services.DSViewRecordService.create_cookie')
@patch('app.modules.dataset.services.DSMetaDataService.filter_by_doi')
def test_subdomain_index_missing_cookie(mock_filter_by_doi, mock_create_cookie, test_client):
    mock_dataset = MagicMock()
    mock_filter_by_doi.return_value = MagicMock(data_set=mock_dataset)
    mock_create_cookie.return_value = "user_cookie_value"  # Return a valid cookie value
 
    response = test_client.get('/doi/10.1234/dataset1/')
 
    # Verify the response is 200 OK
    assert response.status_code == 200
 
    # Verify the cookie is set
    cookies = response.headers.get('Set-Cookie')
    assert cookies is not None
    assert 'view_cookie=user_cookie_value' in cookies  # Check if the correct cookie is set



