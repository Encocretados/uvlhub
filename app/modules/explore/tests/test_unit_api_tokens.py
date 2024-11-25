# app/modules/dataset/tests/test_unit_api_tokens.py

import pytest
from app.modules.auth.services import generate_access_token
import jwt
from datetime import datetime

@pytest.fixture
def test_client():
    from app import app as flask_app
    flask_app.config["SECRET_KEY"] = "b2c9e8f4a6d7c3e1f8b4a2d9e7c6f5a3"
    with flask_app.test_client() as client:
        yield client

@pytest.fixture
def test_user():
    class User:
        def __init__(self, id, email):
            self.id = id
            self.email = email
    return User(id=1, email="user1@example.com")

def test_generate_access_token(test_client, test_user):
    """
    Verifica que el token generado sea válido y contenga el user_id correcto.
    """
    # Generar el token
    token = generate_access_token(test_user.id)

    # Decodificar el token usando el SECRET_KEY fijo para pruebas
    secret_key = test_client.application.config["SECRET_KEY"]
    decoded = jwt.decode(token, secret_key, algorithms=["HS256"])

    # Verificar que el user_id en el token sea correcto
    assert decoded["user_id"] == test_user.id