import pytest
from flask import Flask
from app.modules.fakenodo import fakenodo_bp  # Importa el blueprint fakenodo_bp

# Crear una aplicación de Flask para las pruebas
@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(fakenodo_bp)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

# Prueba para la ruta GET /fakenodo/api
def test_test_connection_fakenodo(client):
    response = client.get("/fakenodo/api")
    assert response.status_code == 200
    assert response.get_json() == {
        "status": "success",
        "message": "The API of Fakenodo connected successfully"
    }

# Prueba para la ruta POST /fakenodo/api
def test_create_fakenodo(client):
    response = client.post("/fakenodo/api")
    assert response.status_code == 201
    assert response.get_json() == {
        "status": "success",
        "message": "The deposition of Fakenodo was created"
    }

# Prueba para la ruta POST /fakenodo/api/<id>/deposition
def test_deposition_files_fakenodo(client):
    deposition_id = "123"
    response = client.post(f"/fakenodo/api/{deposition_id}/deposition")
    assert response.status_code == 201
    assert response.get_json() == {
        "status": "success",
        "message": f"The deposition {deposition_id} was successfully created"
    }

# Prueba para la ruta DELETE /fakenodo/api/<id>
def test_delete_deposition_fakenodo(client):
    deposition_id = "123"
    response = client.delete(f"/fakenodo/api/{deposition_id}")
    assert response.status_code == 200
    assert response.get_json() == {
        "status": "success",
        "message": f"The deposition {deposition_id} was succesfully deleted"
    }

# Prueba para la ruta POST /fakenodo/api/<id>/resources/submit
def test_publish_deposition_fakenodo(client):
    deposition_id = "123"
    response = client.post(f"/fakenodo/api/{deposition_id}/resources/submit")
    assert response.status_code == 202
    assert response.get_json() == {
        "status": "success",
        "message": f"Deposition with ID {deposition_id} succesfully published in the API of Fakenodo"
    }

# Prueba para la ruta GET /fakenodo/api/<id>
def test_get_deposition_fakenodo(client):
    deposition_id = "123"
    response = client.get(f"/fakenodo/api/{deposition_id}")
    assert response.status_code == 200
    assert response.get_json() == {
        "status": "success",
        "message": f"The deposition with ID {deposition_id} successfully gotten in the API of Fakenodo",
        "doi": "10.5072/fakenodo.123456"
    }
