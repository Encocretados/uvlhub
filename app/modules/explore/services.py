from app.modules.explore.repositories import ExploreRepository
from core.services.BaseService import BaseService


class ExploreService(BaseService):
    def __init__(self):
        # Inicializa la clase base con el repositorio correspondiente
        super().__init__(ExploreRepository())

    def filter(
        self,
        query="",
        sorting="newest",
        publication_type="any",
        tags=[],
        after_date=None,
        before_date=None,
        min_size=None,
        max_size=None,
        author_name=None,
        **kwargs
    ):
        # Invoca el método de filtrado del repositorio con los parámetros proporcionados
        return self.repository.filter(
            query=query,
            sorting=sorting,
            publication_type=publication_type,
            tags=tags,
            after_date=after_date,
            before_date=before_date,
            min_size=min_size,
            max_size=max_size,
            author_name=author_name,
            **kwargs
        )

    def advance_filter(
        self,
        query="",
        sorting="newest",
        publication_type="any",
        tags=[],
        after_date=None,
        before_date=None,
        min_size=None,
        max_size=None,
        size_unit="KB",
        author_name=None,
    ):
        return self.repository.filter(
            query=query,
            sorting=sorting,
            publication_type=publication_type,
            tags=tags,
            after_date=after_date,
            before_date=before_date,
            min_size=min_size,
            max_size=max_size,
            size_unit=size_unit,
            author_name=author_name,
        )
