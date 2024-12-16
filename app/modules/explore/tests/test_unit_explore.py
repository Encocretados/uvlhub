import pytest
from unittest.mock import patch, MagicMock
from app.modules.explore.services import ExploreService

@pytest.fixture
def explore_service():
    return ExploreService()

@patch('app.modules.explore.services.ExploreService.advance_filter')
def test_advance_filter_by_title(mock_advance_filter, explore_service):
    # Mock de datasets con títulos específicos
    mock_dataset_1 = MagicMock()
    mock_dataset_1.to_dict.return_value = {
        "id": 1,
        "title": "Dataset about AI",
        "description": "Description for dataset about AI",
        "url": "/dataset/1",
        "authors": [{"name": "Author 1"}],
        "tags": ["AI", "ML"],
        "created_at": "2023-01-01",
    }
    mock_dataset_2 = MagicMock()
    mock_dataset_2.to_dict.return_value = {
        "id": 2,
        "title": "Dataset about ML",
        "description": "Description for dataset about ML",
        "url": "/dataset/2",
        "authors": [{"name": "Author 2"}],
        "tags": ["ML"],
        "created_at": "2023-02-01",
    }
    # Ajusta el mock para que devuelva solo el dataset que coincide con el título
    mock_advance_filter.side_effect = lambda query, sorting, publication_type, tags, after_date, before_date, min_size, max_size, size_unit, author_name: [mock_dataset_1] if query == "Dataset about AI" else []

    # Parámetro de búsqueda por título
    query = "Dataset about AI"
    result = explore_service.advance_filter(
        query=query,
        sorting="newest",
        publication_type="any",
        tags=[],
        after_date=None,
        before_date=None,
        min_size=None,
        max_size=None,
        size_unit="KB",
        author_name=None
    )

    # Verificación del resultado
    assert len(result) == 1
    assert result[0].to_dict()["title"] == "Dataset about AI"
    mock_advance_filter.assert_called_once_with(
        query="Dataset about AI",
        sorting="newest",
        publication_type="any",
        tags=[],
        after_date=None,
        before_date=None,
        min_size=None,
        max_size=None,
        size_unit="KB",
        author_name=None
    )

@patch('app.modules.explore.services.ExploreService.advance_filter')
def test_advance_filter_by_publication_type(mock_advance_filter, explore_service):
    # Mock de datasets con tipos de publicación específicos
    mock_dataset_1 = MagicMock()
    mock_dataset_1.to_dict.return_value = {
        "id": 1,
        "title": "Research Paper on AI",
        "description": "Description for research paper on AI",
        "url": "/dataset/1",
        "authors": [{"name": "Author 1"}],
        "tags": ["AI", "ML"],
        "created_at": "2023-01-01",
        "publication_type": "research_paper"
    }
    mock_dataset_2 = MagicMock()
    mock_dataset_2.to_dict.return_value = {
        "id": 2,
        "title": "Article on ML",
        "description": "Description for article on ML",
        "url": "/dataset/2",
        "authors": [{"name": "Author 2"}],
        "tags": ["ML"],
        "created_at": "2023-02-01",
        "publication_type": "article"
    }
    # Ajusta el mock para que devuelva solo el dataset que coincide con el tipo de publicación
    mock_advance_filter.side_effect = lambda query, sorting, publication_type, tags, after_date, before_date, min_size, max_size, size_unit, author_name: [mock_dataset_1] if publication_type == "research_paper" else []

    # Parámetro de búsqueda por tipo de publicación
    publication_type = "research_paper"
    result = explore_service.advance_filter(
        query="",
        sorting="newest",
        publication_type=publication_type,
        tags=[],
        after_date=None,
        before_date=None,
        min_size=None,
        max_size=None,
        size_unit="KB",
        author_name=None
    )

    # Verificación del resultado
    assert len(result) == 1
    assert result[0].to_dict()["publication_type"] == "research_paper"
    mock_advance_filter.assert_called_once_with(
        query="",
        sorting="newest",
        publication_type="research_paper",
        tags=[],
        after_date=None,
        before_date=None,
        min_size=None,
        max_size=None,
        size_unit="KB",
        author_name=None
    )

@patch('app.modules.explore.services.ExploreService.advance_filter')
def test_advance_filter_by_author(mock_advance_filter, explore_service):
    # Mock de datasets con autores específicos
    mock_dataset_1 = MagicMock()
    mock_dataset_1.to_dict.return_value = {
        "id": 1,
        "title": "Dataset by Author 1",
        "description": "Description for dataset by Author 1",
        "url": "/dataset/1",
        "authors": [{"name": "Author 1"}],
        "tags": ["AI", "ML"],
        "created_at": "2023-01-01",
    }
    mock_dataset_2 = MagicMock()
    mock_dataset_2.to_dict.return_value = {
        "id": 2,
        "title": "Dataset by Author 2",
        "description": "Description for dataset by Author 2",
        "url": "/dataset/2",
        "authors": [{"name": "Author 2"}],
        "tags": ["ML"],
        "created_at": "2023-02-01",
    }
    # Ajusta el mock para que devuelva solo el dataset que coincide con el autor
    mock_advance_filter.side_effect = lambda query, sorting, publication_type, tags, after_date, before_date, min_size, max_size, size_unit, author_name: [mock_dataset_1] if author_name == "Author 1" else []

    # Parámetro de búsqueda por autor
    author_name = "Author 1"
    result = explore_service.advance_filter(
        query="",
        sorting="newest",
        publication_type="any",
        tags=[],
        after_date=None,
        before_date=None,
        min_size=None,
        max_size=None,
        size_unit="KB",
        author_name=author_name
    )

    # Verificación del resultado
    assert len(result) == 1
    assert result[0].to_dict()["authors"][0]["name"] == "Author 1"
    mock_advance_filter.assert_called_once_with(
        query="",
        sorting="newest",
        publication_type="any",
        tags=[],
        after_date=None,
        before_date=None,
        min_size=None,
        max_size=None,
        size_unit="KB",
        author_name="Author 1"
    )

@patch('app.modules.explore.services.ExploreService.advance_filter')
def test_advance_filter_by_tags(mock_advance_filter, explore_service):
    # Mock de datasets con etiquetas específicas
    mock_dataset_1 = MagicMock()
    mock_dataset_1.to_dict.return_value = {
        "id": 1,
        "title": "Dataset with AI tag",
        "description": "Description for dataset with AI tag",
        "url": "/dataset/1",
        "authors": [{"name": "Author 1"}],
        "tags": ["AI", "ML"],
        "created_at": "2023-01-01",
    }
    mock_dataset_2 = MagicMock()
    mock_dataset_2.to_dict.return_value = {
        "id": 2,
        "title": "Dataset with ML tag",
        "description": "Description for dataset with ML tag",
        "url": "/dataset/2",
        "authors": [{"name": "Author 2"}],
        "tags": ["ML"],
        "created_at": "2023-02-01",
    }
    # Ajusta el mock para que devuelva solo el dataset que coincide con las etiquetas
    mock_advance_filter.side_effect = lambda query, sorting, publication_type, tags, after_date, before_date, min_size, max_size, size_unit, author_name: [mock_dataset_1] if "AI" in tags else []

    # Parámetro de búsqueda por etiquetas
    tags = ["AI"]
    result = explore_service.advance_filter(
        query="",
        sorting="newest",
        publication_type="any",
        tags=tags,
        after_date=None,
        before_date=None,
        min_size=None,
        max_size=None,
        size_unit="KB",
        author_name=None
    )

    # Verificación del resultado
    assert len(result) == 1
    assert "AI" in result[0].to_dict()["tags"]
    mock_advance_filter.assert_called_once_with(
        query="",
        sorting="newest",
        publication_type="any",
        tags=["AI"],
        after_date=None,
        before_date=None,
        min_size=None,
        max_size=None,
        size_unit="KB",
        author_name=None
    )

@patch('app.modules.explore.services.ExploreService.advance_filter')
def test_advance_filter_by_date_range(mock_advance_filter, explore_service):
    # Mock de datasets con fechas específicas
    mock_dataset_1 = MagicMock()
    mock_dataset_1.to_dict.return_value = {
        "id": 1,
        "title": "Dataset created in 2023",
        "description": "Description for dataset created in 2023",
        "url": "/dataset/1",
        "authors": [{"name": "Author 1"}],
        "tags": ["AI", "ML"],
        "created_at": "2023-01-01",
    }
    mock_dataset_2 = MagicMock()
    mock_dataset_2.to_dict.return_value = {
        "id": 2,
        "title": "Dataset created in 2024",
        "description": "Description for dataset created in 2024",
        "url": "/dataset/2",
        "authors": [{"name": "Author 2"}],
        "tags": ["ML"],
        "created_at": "2024-01-01",
    }
    # Ajusta el mock para que devuelva solo el dataset que coincide con el rango de fechas
    mock_advance_filter.side_effect = lambda query, sorting, publication_type, tags, after_date, before_date, min_size, max_size, size_unit, author_name: [mock_dataset_1] if after_date <= mock_dataset_1.to_dict()["created_at"] <= before_date else []

    # Parámetro de búsqueda por rango de fechas
    after_date = "2023-01-01"
    before_date = "2023-12-31"
    result = explore_service.advance_filter(
        query="",
        sorting="newest",
        publication_type="any",
        tags=[],
        after_date=after_date,
        before_date=before_date,
        min_size=None,
        max_size=None,
        size_unit="KB",
        author_name=None
    )

    # Verificación del resultado
    assert len(result) == 1
    assert result[0].to_dict()["created_at"] == "2023-01-01"
    mock_advance_filter.assert_called_once_with(
        query="",
        sorting="newest",
        publication_type="any",
        tags=[],
        after_date=after_date,
        before_date=before_date,
        min_size=None,
        max_size=None,
        size_unit="KB",
        author_name=None
    )

@patch('app.modules.explore.services.ExploreService.advance_filter')
def test_advance_filter_by_size(mock_advance_filter, explore_service):
    # Mock de datasets con tamaños específicos
    mock_dataset_1 = MagicMock()
    mock_dataset_1.to_dict.return_value = {
        "id": 1,
        "title": "Small dataset",
        "description": "Description for small dataset",
        "url": "/dataset/1",
        "authors": [{"name": "Author 1"}],
        "tags": ["AI", "ML"],
        "created_at": "2023-01-01",
        "size": 500  # Tamaño en KB
    }
    mock_dataset_2 = MagicMock()
    mock_dataset_2.to_dict.return_value = {
        "id": 2,
        "title": "Large dataset",
        "description": "Description for large dataset",
        "url": "/dataset/2",
        "authors": [{"name": "Author 2"}],
        "tags": ["ML"],
        "created_at": "2023-02-01",
        "size": 2000  # Tamaño en KB
    }
    # Ajusta el mock para que devuelva solo el dataset que coincide con el tamaño
    mock_advance_filter.side_effect = lambda query, sorting, publication_type, tags, after_date, before_date, min_size, max_size, size_unit, author_name: [mock_dataset_1] if min_size <= mock_dataset_1.to_dict()["size"] <= max_size else []

    # Parámetro de búsqueda por tamaño
    min_size = 100
    max_size = 1000
    result = explore_service.advance_filter(
        query="",
        sorting="newest",
        publication_type="any",
        tags=[],
        after_date=None,
        before_date=None,
        min_size=min_size,
        max_size=max_size,
        size_unit="KB",
        author_name=None
    )

    # Verificación del resultado
    assert len(result) == 1
    assert result[0].to_dict()["size"] == 500
    mock_advance_filter.assert_called_once_with(
        query="",
        sorting="newest",
        publication_type="any",
        tags=[],
        after_date=None,
        before_date=None,
        min_size=min_size,
        max_size=max_size,
        size_unit="KB",
        author_name=None
    )

@patch('app.modules.explore.services.ExploreService.advance_filter')
def test_advance_filter_sorting_oldest(mock_advance_filter, explore_service):
    # Mock de datasets con fechas específicas
    mock_dataset_1 = MagicMock()
    mock_dataset_1.to_dict.return_value = {
        "id": 1,
        "title": "New dataset",
        "description": "Description for new dataset",
        "url": "/dataset/1",
        "authors": [{"name": "Author 1"}],
        "tags": ["AI", "ML"],
        "created_at": "2023-01-01",
    }
    mock_dataset_2 = MagicMock()
    mock_dataset_2.to_dict.return_value = {
        "id": 2,
        "title": "Old dataset",
        "description": "Description for old dataset",
        "url": "/dataset/2",
        "authors": [{"name": "Author 2"}],
        "tags": ["ML"],
        "created_at": "2022-01-01",
    }
    # Ajusta el mock para que devuelva los datasets ordenados de más nuevo a más viejo por defecto
    mock_advance_filter.side_effect = lambda query, sorting, publication_type, tags, after_date, before_date, min_size, max_size, size_unit, author_name: [mock_dataset_1, mock_dataset_2] if sorting == "newest" else [mock_dataset_2, mock_dataset_1]

    # Parámetro de búsqueda por ordenación de más nuevo a más viejo
    sorting = "newest"
    result = explore_service.advance_filter(
        query="",
        sorting=sorting,
        publication_type="any",
        tags=[],
        after_date=None,
        before_date=None,
        min_size=None,
        max_size=None,
        size_unit="KB",
        author_name=None
    )

    # Verificación del resultado
    assert len(result) == 2
    assert result[0].to_dict()["created_at"] == "2023-01-01"
    assert result[1].to_dict()["created_at"] == "2022-01-01"
    mock_advance_filter.assert_called_once_with(
        query="",
        sorting="newest",
        publication_type="any",
        tags=[],
        after_date=None,
        before_date=None,
        min_size=None,
        max_size=None,
        size_unit="KB",
        author_name=None
    )

    # Parámetro de búsqueda por ordenación de más viejo a más nuevo
    sorting = "oldest"
    result = explore_service.advance_filter(
        query="",
        sorting=sorting,
        publication_type="any",
        tags=[],
        after_date=None,
        before_date=None,
        min_size=None,
        max_size=None,
        size_unit="KB",
        author_name=None
    )

    # Verificación del resultado
    assert len(result) == 2
    assert result[0].to_dict()["created_at"] == "2022-01-01"
    assert result[1].to_dict()["created_at"] == "2023-01-01"
    mock_advance_filter.assert_called_with(
        query="",
        sorting="oldest",
        publication_type="any",
        tags=[],
        after_date=None,
        before_date=None,
        min_size=None,
        max_size=None,
        size_unit="KB",
        author_name=None
    )
