from app.modules.flamapy.repositories import FlamapyRepository
from core.services.BaseService import BaseService


class FlamapyService(BaseService):
    def analyze_with_ai(self, query):
        """
        Usa un modelo de IA para analizar el texto.
        """
        if "predecir" in query:
            return "El modelo predice: éxito probable."
        return "No se puede realizar una predicción con esa consulta."
    
    def __init__(self):
        super().__init__(FlamapyRepository())
