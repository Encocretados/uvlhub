# ai_services.py
from transformers import pipeline

class AIService:
    def __init__(self):
        """
        Inicializa el modelo de IA.
        """
        self.model = pipeline("text-generation", model="openai-community/gpt2", top_k=50, top_p=0.95)

    def process_query(self, query):
        """
        Procesa la consulta con el modelo de IA.
        """
        return self.model(query, max_length=100, num_return_sequences=1)[0]["generated_text"]
