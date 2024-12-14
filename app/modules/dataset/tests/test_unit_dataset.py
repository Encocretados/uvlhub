import pytest
from datetime import datetime
from unittest.mock import MagicMock
from app.modules.dataset.models import DataSet, DSMetaData
from app.modules.dataset.repositories import DataSetRepository


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

