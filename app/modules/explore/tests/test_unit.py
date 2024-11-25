import pytest
from app.modules.explore.services import ExploreService

@pytest.fixture
def explore_service():
    return ExploreService()

def test_advanced_filter(explore_service):
    filters = {
        "date_range": ["2023-01-01", "2023-12-31"],
        "attributes": {"type": "report"},
        "keywords": ["data"]
    }
    results = explore_service.advanced_filter(**filters)
    assert len(results) > 0
    for result in results:
        assert "2023" in result.date
        assert result.type == "report"
        assert "data" in result.description