from flask import Flask, request, jsonify, render_template, Blueprint
import os
from google.cloud import dialogflow

# Crear el Blueprint
ia_bp = Blueprint('ia_bp', __name__, template_folder='templates')

# Configuración de Dialogflow
DIALOGFLOW_PROJECT_ID = 'uvlhubia-umhn'
DIALOGFLOW_LANGUAGE_CODE = 'es'  # O el idioma que prefieras
GOOGLE_APPLICATION_CREDENTIALS = 'uvlhubia-umhn-a.json'

# Establecer la variable de entorno de credenciales de Google Cloud
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS

# Ruta para mostrar el formulario de la IA y manejar la solicitud POST
@ia_bp.route('/ia', methods=['GET', 'POST'])
def ia():
    if request.method == 'GET':
        print("Formulario de IA solicitado")  # Depuración
        return render_template('ia.html')
    elif request.method == 'POST':
        try:
            print("Solicitud recibida en /ia")  # Depuración
            user_message = request.json.get('question')
            user_id = request.json.get('user_id')

            # Verificar que los parámetros estén presentes
            if not user_message or not user_id:
                print("Error: Faltan parámetros necesarios.")  # Depuración
                return jsonify({"error": "Faltan parámetros necesarios."}), 400

            print(f"Parámetros recibidos: question='{user_message}', user_id='{user_id}'")  # Depuración

            # Crear una sesión de Dialogflow
            session_client = dialogflow.SessionsClient()
            session = session_client.session_path(DIALOGFLOW_PROJECT_ID, user_id)

            # Construir el mensaje de consulta
            text_input = dialogflow.TextInput(text=user_message, language_code=DIALOGFLOW_LANGUAGE_CODE)
            query_input = dialogflow.QueryInput(text=text_input)

            # Hacer la solicitud a Dialogflow
            response = session_client.detect_intent(session=session, query_input=query_input)

            # Extraer la respuesta de Dialogflow
            intent_response = response.query_result.fulfillment_text

            print(f"Respuesta de Dialogflow: {intent_response}")  # Depuración

            return jsonify({"answer": intent_response})

        except Exception as e:
            print(f"Error en /ia: {e}")  # Depuración
            return jsonify({"error": str(e)}), 500