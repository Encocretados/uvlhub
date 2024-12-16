from unittest.mock import MagicMock, patch

import pytest
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

    mock_response = MagicMock()
    mock_response.query_result.fulfillment_text = "Respuesta simulada de Dialogflow"

    mock_sessions_client.return_value.session_path.return_value = "mock_session_path"
    mock_sessions_client.return_value.detect_intent.return_value = mock_response

    ia_service = IaService()

    with app.test_request_context(json={"question": "Hola", "user_id": "123"}):
        response = ia_service.ia_service()
        data = response.get_json()

        assert response.status_code == 200
        assert data["response"] == "Respuesta simulada de Dialogflow"


@patch("app.modules.ia.services.dialogflow.SessionsClient")
def test_ia_service_missing_params(mock_sessions_client, app, client):
    """Prueba el caso en que faltan parámetros en la solicitud."""
    ia_service = IaService()

    with app.test_request_context(json={"question": "Hola"}):  # Falta el user_id
        response, status_code = ia_service.ia_service()
        data = response.get_json()

        assert status_code == 400
        assert "error" in data
        assert data["error"] == "Faltan parámetros necesarios."


@patch("app.modules.ia.services.dialogflow.SessionsClient")
def test_ia_service_dialogflow_error(mock_sessions_client, app, client):
    """Prueba el caso en que ocurre un error en Dialogflow."""

    mock_sessions_client.return_value.detect_intent.side_effect = Exception(
        "Error de Dialogflow simulado"
    )

    ia_service = IaService()

    with app.test_request_context(json={"question": "Hola", "user_id": "123"}):
        response, status_code = ia_service.ia_service()
        data = response.get_json()

        assert status_code == 500
        assert "error" in data
        assert data["error"] == "Error de Dialogflow simulado"


@patch("app.modules.ia.services.dialogflow.SessionsClient")
def test_ia_service_unexpected_dialogflow_response(mock_sessions_client, app, client):
    """Prueba el caso en que Dialogflow devuelve una respuesta inesperada."""
    mock_response = MagicMock()
    mock_response.query_result = None

    mock_sessions_client.return_value.session_path.return_value = "mock_session_path"
    mock_sessions_client.return_value.detect_intent.return_value = mock_response

    ia_service = IaService()

    with app.test_request_context(json={"question": "Hola", "user_id": "123"}):
        response, status_code = ia_service.ia_service()
        data = response.get_json()

        assert status_code == 500
        assert "error" in data
        assert "Estructura inesperada" in data["error"]


@patch("app.modules.ia.services.dialogflow.SessionsClient")
def test_ia_service_empty_question(mock_sessions_client, app, client):
    """Prueba el caso cuando el campo 'question' está vacío."""

    ia_service = IaService()

    with app.test_request_context(
        json={"question": "", "user_id": "123"}
    ):  # Pregunta vacía
        response, status_code = ia_service.ia_service()
        data = response.get_json()

        assert status_code == 400
        assert "error" in data
        assert data["error"] == "El campo 'question' no puede estar vacío."


@patch("app.modules.ia.services.dialogflow.SessionsClient")
def test_ia_service_empty_user_id(mock_sessions_client, app, client):
    """Prueba el caso cuando el campo 'user_id' está vacío."""

    ia_service = IaService()

    with app.test_request_context(
        json={"question": "Hola", "user_id": ""}
    ):  # user_id vacío
        response, status_code = ia_service.ia_service()
        data = response.get_json()

        assert status_code == 400
        assert "error" in data
        assert data["error"] == "Faltan parámetros necesarios."


@patch("app.modules.ia.services.dialogflow.SessionsClient")
def test_ia_service_empty_fulfillment_text(mock_sessions_client, app, client):
    """Prueba el caso en que Dialogflow devuelve un fulfillment_text vacío."""

    mock_response = MagicMock()
    mock_response.query_result.fulfillment_text = ""  # Respuesta vacía de Dialogflow

    mock_sessions_client.return_value.session_path.return_value = "mock_session_path"
    mock_sessions_client.return_value.detect_intent.return_value = mock_response

    ia_service = IaService()

    with app.test_request_context(json={"question": "Hola", "user_id": "123"}):
        response, status_code = ia_service.ia_service()
        data = response.get_json()

        assert status_code == 500
        assert "error" in data
        assert data["error"] == "Respuesta vacía de Dialogflow."


@patch("app.modules.ia.services.dialogflow.SessionsClient")
def test_ia_service_dialogflow_connection_error(mock_sessions_client, app, client):
    """Prueba el caso en que ocurre un error de conexión a Dialogflow."""

    # Configurar el mock para simular un error de conexión
    mock_sessions_client.side_effect = Exception("Error de conexión a Dialogflow")

    ia_service = IaService()

    with app.test_request_context(json={"question": "Hola", "user_id": "123"}):
        response, status_code = ia_service.ia_service()
        data = response.get_json()

        assert status_code == 500
        assert "error" in data
        assert data["error"] == "Error de conexión a Dialogflow"


@patch("app.modules.ia.services.dialogflow.SessionsClient")
def test_ia_service_no_intent_detected(mock_sessions_client, app, client):
    """Prueba el caso en que Dialogflow no detecta ninguna intención."""

    mock_response = MagicMock()
    mock_response.query_result.fulfillment_text = ""
    mock_response.query_result.intent = None

    mock_sessions_client.return_value.session_path.return_value = "mock_session_path"
    mock_sessions_client.return_value.detect_intent.return_value = mock_response

    ia_service = IaService()

    with app.test_request_context(json={"question": "Hola", "user_id": "123"}):
        response, status_code = ia_service.ia_service()
        data = response.get_json()

        assert status_code == 500
        assert "error" in data
        assert data["error"] == "Respuesta vacía de Dialogflow."


@patch("app.modules.ia.services.dialogflow.SessionsClient")
def test_ia_service_invalid_json_body(mock_sessions_client, app, client):
    """Prueba el caso en que el cuerpo de la solicitud no contiene un JSON válido."""

    ia_service = IaService()

    # Simular una solicitud con cuerpo inválido (no es JSON)
    with app.test_request_context(data="Texto no JSON", content_type="text/plain"):
        response, status_code = ia_service.ia_service()
        data = response.get_json()

        assert status_code == 400
        assert "error" in data
        assert data["error"] == "El cuerpo de la solicitud debe ser un JSON válido."


@patch("app.modules.ia.services.dialogflow.SessionsClient")
def test_ia_service_excessively_long_question(mock_sessions_client, app, client):
    """Prueba el caso en que el campo 'question' es excesivamente largo."""

    ia_service = IaService()

    # Crear un mensaje excesivamente largo
    long_message = "a" * 10001  # Por ejemplo, 10,001 caracteres

    with app.test_request_context(json={"question": long_message, "user_id": "123"}):
        response, status_code = ia_service.ia_service()
        data = response.get_json()

        assert status_code == 400
        assert "error" in data
        assert (
            data["error"] == "El campo 'question' excede la longitud máxima permitida."
        )


@patch("app.modules.ia.services.dialogflow.SessionsClient")
def test_ia_service_missing_question(mock_sessions_client, app, client):
    """Prueba el caso cuando el campo 'question' está ausente en la solicitud."""

    ia_service = IaService()

    # Simular una solicitud sin el campo 'question' (solo con 'user_id')
    with app.test_request_context(json={"user_id": "123"}):  # Falta el campo 'question'
        response, status_code = ia_service.ia_service()
        data = response.get_json()

        assert status_code == 400
        assert "error" in data
        assert data["error"] == "El campo 'question' no puede estar vacío."
