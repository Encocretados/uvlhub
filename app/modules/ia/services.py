import os
from flask import Flask, request, jsonify, render_template
from google.cloud import dialogflow
from core.services.BaseService import BaseService

DIALOGFLOW_PROJECT_ID = 'uvlhubia-umhn'
DIALOGFLOW_LANGUAGE_CODE = 'es'  # O el idioma que prefieras
GOOGLE_APPLICATION_CREDENTIALS = 'uvlhubia-ia.json'
class IaService(BaseService):
    def __init__(self):
        super().__init__(None)  # No es necesario un repositorio específico aquí
        # Aquí puedes inicializar otros componentes necesarios, si es necesario.

    def ia_form(self):
        return render_template('ia.html')

    def ia_service(self):
        try:
            
            if not request.is_json:
                return jsonify({"error": "El cuerpo de la solicitud debe ser un JSON válido."}), 400
        
            user_message = request.json.get('question')
            session_id = request.json.get('user_id')

            if not user_message:
                return jsonify({"error": "El campo 'question' no puede estar vacío."}), 400
            if len(user_message) > 10000:  # Ejemplo: Limitar a 10,000 caracteres
                return jsonify({"error": "El campo 'question' excede la longitud máxima permitida."}), 400
            if not session_id:
                return jsonify({"error": "Faltan parámetros necesarios."}), 400

            
            session_client = dialogflow.SessionsClient()
            session = session_client.session_path(DIALOGFLOW_PROJECT_ID, session_id)

            
            text_input = dialogflow.TextInput(text=user_message, language_code=DIALOGFLOW_LANGUAGE_CODE)
            query_input = dialogflow.QueryInput(text=text_input)

            
            response = session_client.detect_intent(session=session, query_input=query_input)
            
            if response.query_result is None:
                raise ValueError("Estructura inesperada en la respuesta de Dialogflow.")
        
            intent_response = response.query_result.fulfillment_text

            if not intent_response:
                raise ValueError("Respuesta vacía de Dialogflow.")

            return jsonify({"response": intent_response})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    
