import pytest
from unittest.mock import patch, MagicMock
from flask import Flask, jsonify, request
from app.modules.ia.services import IaService


@pytest.fixture
def app():
    """Crea una aplicación Flask de prueba."""
    app = Flask(__name__)
    app.testing = True
    return app


@pytest.fixture
def client(app):
    """Cliente de prueba para realizar solicitudes."""
    return app.test_client()


@patch("app.modules.ia.services.dialogflow.SessionsClient")
def test_ia_service_success(mock_sessions_client, app, client):
    """Prueba el caso exitoso para ia_service."""

    # Simula un cliente y una respuesta de Dialogflow
    mock_session = MagicMock()
    mock_response = MagicMock()
    mock_response.query_result.fulfillment_text = "Respuesta simulada de Dialogflow"

    # Configura el cliente simulado
    mock_sessions_client.return_value.session_path.return_value = "mock_session_path"
    mock_sessions_client.return_value.detect_intent.return_value = mock_response

    ia_service = IaService()

    with app.test_request_context(json={"question": "Hola", "user_id": "123"}):
        response = ia_service.ia_service()
        data = response.get_json()

        # Verifica que la respuesta sea la esperada
        assert response.status_code == 200
        assert data["response"] == "Respuesta simulada de Dialogflow"


@patch("app.modules.ia.services.dialogflow.SessionsClient")
def test_ia_service_missing_params(mock_sessions_client, app, client):
    """Prueba el caso en que faltan parámetros en la solicitud."""
    ia_service = IaService()

    with app.test_request_context(json={"question": "Hola"}):  # Falta el user_id
        response, status_code = ia_service.ia_service()
        data = response.get_json()

        # Verifica que se devuelva un error de parámetros faltantes
        assert status_code == 400
        assert "error" in data
        assert data["error"] == "Faltan parámetros necesarios."


@patch("app.modules.ia.services.dialogflow.SessionsClient")
def test_ia_service_dialogflow_error(mock_sessions_client, app, client):
    """Prueba el caso en que ocurre un error en Dialogflow."""
    # Simula un cliente de Dialogflow que lanza una excepción
    mock_sessions_client.return_value.detect_intent.side_effect = Exception("Error de Dialogflow simulado")

    ia_service = IaService()

    with app.test_request_context(json={"question": "Hola", "user_id": "123"}):
        response, status_code = ia_service.ia_service()
        data = response.get_json()

        # Verifica que se devuelva un error de Dialogflow
        assert status_code == 500
        assert "error" in data
        assert data["error"] == "Error de Dialogflow simulado"