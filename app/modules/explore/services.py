from app.modules.explore.repositories import ExploreRepository
from core.services.BaseService import BaseService


class ExploreService(BaseService):
    def generate_analysis(self, query):
        """
        Realiza un análisis basado en la consulta del asistente.
        """
        if "explorar" in query:
            return "Aquí tienes un resumen de los datos."
        return "No se encontraron datos para explorar."
    
    def __init__(self):
        super().__init__(ExploreRepository())

    def filter(self, query="", sorting="newest", publication_type="any", tags=[], **kwargs):
        return self.repository.filter(query, sorting, publication_type, tags, **kwargs)
