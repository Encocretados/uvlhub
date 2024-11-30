
import torch
from transformers import pipeline

# Verificar si CUDA (GPU) está disponible y usarla si es posible
device = 0 if torch.cuda.is_available() else -1  # 0 para GPU, -1 para CPU

# Inicializar el pipeline de generación de texto con el modelo de IA
modelo_ia = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B", device=device)

def obtener_respuesta_ia(mensaje):
    """
    Procesa el mensaje del usuario y devuelve una respuesta generada por IA.
    """
    # Generar la respuesta del modelo
    resultado = modelo_ia(mensaje, max_length=150, num_return_sequences=1)
    
    # Devolver el texto generado por el modelo
    return resultado[0]['generated_text']
