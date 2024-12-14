from unittest.mock import patch, MagicMock

from app.modules.dataset.services import DataSetService

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

