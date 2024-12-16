import pytest
from flask import url_for

from app import db
from app.modules.auth.models import User
from app.modules.community.models import Community


# Fixture para configurar el cliente de prueba
@pytest.fixture(scope="module")
def test_client(test_client):
    """
    Extends the test_client fixture to add additional specific data for module testing.
    for module testing (por example, new users)
    """
    with test_client.application.app_context():
        user_test = User(email="user@example.com", password="test1234")
        db.session.add(user_test)
        db.session.commit()

    yield test_client


# Test de borrado de una comunidad siendo el creador
def test_delete_community_success(test_client):

    test_client.post(
        "/login", data={"email": "user@example.com", "password": "test1234"}
    )

    with test_client.application.app_context():
        user = User.query.filter_by(email="user@example.com").first()

    data = {
        "name": "Delete Community",
        "description": "This is a delete community.",
        "user": user,  # Pasar el objeto user completo
    }

    response = test_client.post("/community/create", data=data, follow_redirects=True)

    community = Community.query.filter_by(name="Delete Community").first()
    assert community is not None, "La comunidad no se ha creado"

    # Enviar la solicitud de eliminación
    response = test_client.post(
        f"/community/{community.id}/delete", follow_redirects=True
    )

    assert (
        response.status_code == 200
    ), "El estado debería ser 200 después de borrar la comunidad"

    with test_client.application.app_context():
        deleted_community = Community.query.filter_by(name="Test Community").first()
        assert deleted_community is None, "La comunidad no fue eliminada"

    test_client.get("/logout", follow_redirects=True)


# Test de creación de comunidad
def test_create_community_authenticated(test_client):

    test_client.post(
        "/login", data={"email": "user@example.com", "password": "test1234"}
    )

    with test_client.application.app_context():
        user = User.query.filter_by(email="user@example.com").first()

    data = {
        "name": "Test Community",
        "description": "This is a test community.",
        "user": user,  # Pasar el objeto user completo
    }

    response = test_client.post("/community/create", data=data, follow_redirects=True)

    assert (
        response.status_code == 200
    ), "El estado debería ser 200 después de crear la comunidad"

    # Verificar que la comunidad fue creada
    community = Community.query.filter_by(name="Test Community").first()
    assert community is not None, "La comunidad no fue creada"
    assert (
        community.creator_id == user.id
    ), "El creador de la comunidad no es el usuario correcto"
    assert user in community.members, "El usuario no es miembro de la comunidad"

    test_client.get("/logout", follow_redirects=True)
    db.session.delete(community)


# Test de creación de comunidad sin autenticación
def test_create_community_unauthenticated(test_client):

    with test_client.application.app_context():
        user = User.query.filter_by(email="user@example.com").first()

    data = {
        "name": "Test Community",
        "description": "This is a test community.",
        "user": user,  # Pasar el objeto user completo
    }

    response = test_client.post("/community/create", data=data, follow_redirects=True)

    assert (
        response.status_code == 200
    ), "El estado debería ser 200 después de crear la comunidad"

    # Verificar que la comunidad no fue creada
    community = Community.query.filter_by(name="Test Community").first()
    assert community is None, "La comunidad no debería haber sido creada"
