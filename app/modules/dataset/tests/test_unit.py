import pytest
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



