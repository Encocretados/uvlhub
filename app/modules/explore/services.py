from app.modules.explore.repositories import ExploreRepository
from core.services.BaseService import BaseService


class ExploreService(BaseService):
    def __init__(self):
        super().__init__(ExploreRepository())


    def filter(self, query="", sorting="newest", publication_type="any", tags=[], **kwargs):
        return self.repository.filter(query, sorting, publication_type, tags, **kwargs)

    def advanced_filter(self, date_range=None, attributes=None, keywords=None, **kwargs):
        filters = {
            "date_range": date_range,
            "attributes": attributes,
            "keywords": keywords,
            **kwargs
        }
        return self.repository.advanced_filter(filters)
    
    def clear_filters(self):
        return self.repository.get_all_datasets()
