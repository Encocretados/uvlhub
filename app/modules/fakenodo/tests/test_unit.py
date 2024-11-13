import pytest
from flask import Flask
from app.modules.fakenodo import fakenodo_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(fakenodo_bp)
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_test_connection_fakenodo(client):
    response = client.get("/fakenodo/api")
    assert response.status_code == 200
    assert response.get_json() == {
        "status": "success",
        "message": "The API of Fakenodo connected successfully"
    }


def test_create_fakenodo(client):
    response = client.post("/fakenodo/api")
    assert response.status_code == 201
    assert response.get_json() == {
        "status": "success",
        "message": "The deposition of Fakenodo was created"
    }


def test_deposition_files_fakenodo(client):
    deposition_id = "123"
    response = client.post(f"/fakenodo/api/{deposition_id}/deposition")
    assert response.status_code == 201
    assert response.get_json() == {
        "status": "success",
        "message": f"The deposition {deposition_id} was successfully created"
    }


def test_delete_deposition_fakenodo(client):
    deposition_id = "123"
    response = client.delete(f"/fakenodo/api/{deposition_id}")
    assert response.status_code == 200
    assert response.get_json() == {
        "status": "success",
        "message": f"The deposition {deposition_id} was successfully deleted"
    }


def test_publish_deposition_fakenodo(client):
    deposition_id = "123"
    response = client.post(f"/fakenodo/api/{deposition_id}/resources/submit")
    assert response.status_code == 202
    assert response.get_json() == {
        "status": "success",
        "message": f"Deposition with ID {deposition_id} successfully published in the API of Fakenodo"
    }


def test_get_deposition_fakenodo(client):
    deposition_id = "123"
    response = client.get(f"/fakenodo/api/{deposition_id}")
    assert response.status_code == 200
    assert response.get_json() == {
        "status": "success",
        "message": f"The deposition with ID {deposition_id} successfully retrieved from the API of Fakenodo",
        "doi": "10.5072/fakenodo.123456"
    }
