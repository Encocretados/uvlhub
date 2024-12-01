from transformers import AutoModelForCausalLM, AutoTokenizer
import logging

# Configurar el logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Cargar el modelo y el tokenizador
model_name = "EleutherAI/gpt-neo-1.3B"
logging.info("Cargando el modelo y el tokenizador...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Función principal
def obtener_respuesta_ia(mensaje_usuario):
    """
    Genera una respuesta de IA optimizada para preguntas del usuario.
    Incluye lógica de contexto, detección de saludos y respuestas claras.
    """
    try:
        # Detectar saludos u otras intenciones básicas
        if detectar_saludo(mensaje_usuario):
            return manejar_saludo(mensaje_usuario)

        # Crear el prompt
        prompt = (
            "Eres un asistente virtual amable, útil y preciso. Responde de forma clara y profesional. "
            "Evita divagar o repetir las preguntas del usuario. Si no sabes la respuesta, dilo de manera honesta. "
            f"Usuario: {mensaje_usuario}\nAsistente:"
        )

        logging.info(f"Generando respuesta para: {mensaje_usuario}")

        # Tokenización del prompt
        inputs = tokenizer.encode(prompt, return_tensors="pt")

        # Generación de la respuesta
        outputs = model.generate(
            inputs,
            max_length=150,         # Limitar longitud para evitar respuestas largas
            temperature=0.5,        # Balance entre creatividad y consistencia
            top_p=0.85,             # Mejor selección de palabras probables
            do_sample=True,         # Permitir diversidad en respuestas
            repetition_penalty=1.4  # Penalizar repeticiones
        )

        # Decodificar y limpiar la respuesta
        respuesta_completa = tokenizer.decode(outputs[0], skip_special_tokens=True)
        respuesta = extraer_respuesta(respuesta_completa, mensaje_usuario)

        # Validar y filtrar la respuesta
        respuesta_final = filtrar_respuesta(respuesta, mensaje_usuario)

        logging.info(f"Respuesta generada: {respuesta_final}")
        return respuesta_final

    except Exception as e:
        logging.error(f"Error al generar respuesta: {e}")
        return "Lo siento, ocurrió un error al procesar tu solicitud. Por favor, inténtalo nuevamente."

# Función para extraer la respuesta del modelo
def extraer_respuesta(respuesta_completa, mensaje_usuario):
    """
    Extrae solo la parte de la respuesta generada por el modelo.
    """
    if "Asistente:" in respuesta_completa:
        respuesta = respuesta_completa.split("Asistente:")[-1].strip()
    else:
        respuesta = respuesta_completa.strip()

    # Eliminar cualquier repetición del mensaje del usuario
    if mensaje_usuario.lower() in respuesta.lower():
        respuesta = respuesta.replace(mensaje_usuario, "").strip()
    
    return respuesta

# Función para filtrar y validar la respuesta
def filtrar_respuesta(respuesta, mensaje_usuario):
    """
    Valida la respuesta para asegurar que sea coherente, relevante y no repetitiva.
    """
    # Si la respuesta es demasiado corta o parece irrelevante
    if len(respuesta.split()) < 5 or "no estoy seguro" in respuesta.lower():
        return "Lo siento, no entendí tu pregunta. ¿Podrías reformularla?"

    # Si la respuesta contiene demasiadas repeticiones
    palabras_usuario = set(mensaje_usuario.lower().split())
    palabras_respuesta = set(respuesta.lower().split())
    interseccion = palabras_usuario & palabras_respuesta

    if len(interseccion) > len(palabras_usuario) * 0.6:  # Más del 60% de similitud
        return "Parece que estoy repitiendo tu pregunta. ¿Podrías darme más detalles?"

    # Retornar la respuesta si pasa las validaciones
    return respuesta

# Función para detectar saludos
def detectar_saludo(mensaje_usuario):
    """
    Detecta si el mensaje del usuario es un saludo.
    """
    saludos = ["hola", "buenos días", "buenas tardes", "buenas noches", "qué tal", "saludos"]
    for saludo in saludos:
        if saludo in mensaje_usuario.lower():
            return True
    return False

# Función para manejar saludos
def manejar_saludo(mensaje_usuario):
    """
    Responde específicamente a los saludos detectados.
    """
    return "¡Hola! Espero que estés teniendo un buen día. ¿En qué puedo ayudarte hoy?"

# Función para manejo de fallbacks
def manejar_fallback():
    """
    Devuelve una respuesta predeterminada si no se puede generar una respuesta válida.
    """
    return "Lo siento, no entendí tu pregunta. ¿Podrías explicarla con más detalle?"

# Ejemplo de prueba
if __name__ == "__main__":
    # Entrada de prueba
    mensajes_prueba = [
        "hola", 
        "buenas tardes", 
        "¿Cuál es la capital de Francia?", 
        "Cuéntame una receta para pizza.",
        "¿Cómo estás?",
    ]
    for mensaje in mensajes_prueba:
        respuesta = obtener_respuesta_ia(mensaje)
        print(f"Usuario: {mensaje}")
        print(f"Asistente: {respuesta}")
        print("-" * 40)
