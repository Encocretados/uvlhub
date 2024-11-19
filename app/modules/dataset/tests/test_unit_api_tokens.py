import pytest
import jwt
from datetime import datetime, timedelta
from app.modules.auth.models import User
from app.modules.auth.services import AuthenticationService, generate_access_token
from app import db
from app import ConfigManager as config
from unittest.mock import patch
from app.modules import auth 
from flask import *

SECRET_KEY = "test_secret_key"
ACCESS_TOKEN_EXPIRES = 3600  # 1 hora

def test_generate_access_token(test_client, test_user):
    """
    Verifica que el token generado sea válido y contenga el user_id correcto.
    """
    from app.modules.auth.services import generate_access_token
    import jwt
    from datetime import datetime

    # Generar el token
    token = generate_access_token(test_user.id)

    # Decodificar el token usando el SECRET_KEY fijo para pruebas
    decoded = jwt.decode(token, test_client.application.config["SECRET_KEY"], algorithms=["HS256"])

    # Verificar que contenga el user_id correcto y el campo exp
    assert decoded["user_id"] == test_user.id
    assert "exp" in decoded
    assert datetime.fromtimestamp(decoded["exp"]) > datetime.now()

def test_verify_access_token(test_client, test_user):
    """
    Verifica que el token sea validado correctamente.
    """
    token = generate_access_token(test_user.id)
    user_id = AuthenticationService.verify_access_token(token)
    assert user_id == test_user.id

    # Token expirado
    expired_token = jwt.encode(
        {"user_id": test_user.id, "exp": datetime.now() - timedelta(seconds=100000)},
        test_client.application.config["SECRET_KEY"],
        algorithm="HS256",
    )
    assert AuthenticationService.verify_access_token(expired_token) is None

    # Token inválido
    invalid_token = "invalid.token"
    assert AuthenticationService.verify_access_token(invalid_token) is None


def test_protected_api_route_no_token(test_client):
    """
    Test básico para una ruta protegida que solo pasa si la cookie no se pasa.
    """
 
    response = test_client.get('/protected-api')
    assert response.status_code == 401
    assert response.json["message"] == "Token missing"


def test_protected_api_route_valid_token(test_client,test_user):
    """
    Test básico para una ruta protegida que solo pasa si la cookie es valida.
    """
    token = generate_access_token(test_user.id )
    response = test_client.get('/protected-api', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    assert response.json["message"] == "Valid token"