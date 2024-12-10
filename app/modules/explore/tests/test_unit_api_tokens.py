'''import pytest
from app.modules.auth.services import generate_access_token
import jwt
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

@pytest.fixture
def test_client():
    from app import app as flask_app
    flask_app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")  # Usar la clave desde la variable de entorno
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

    # Decodificar el token usando el SECRET_KEY cargado desde la variable de entorno
    secret_key = test_client.application.config["SECRET_KEY"]
    decoded = jwt.decode(token, secret_key, algorithms=["HS256"])

    # Verificar que el user_id en el token sea correcto
    assert decoded["user_id"] == test_user.id'''
