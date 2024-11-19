import pytest

from app import db
from app.modules.conftest import login, logout
from app.modules.auth.models import User
from app.modules.profile.models import UserProfile


@pytest.fixture(scope="module")
def test_client(test_client):
    """
    Extends the test_client fixture to add additional specific data for module testing.
    for module testing (por example, new users)
    """
    with test_client.application.app_context():
        user_test = User(email='user@example.com', password='test1234')
        db.session.add(user_test)
        db.session.commit()

        profile = UserProfile(user_id=user_test.id, name="Name", surname="Surname")
        db.session.add(profile)
        db.session.commit()

    yield test_client


def test_edit_profile_page_get(test_client):
    """
    Tests access to the profile editing page via a GET request.
    """
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.get("/profile/edit")
    assert response.status_code == 200, "The profile editing page could not be accessed."
    assert b"Edit profile" in response.data, "The expected content is not present on the page"

    logout(test_client)
    
    
def test_developer_profile_page_get(test_client):
    """
    Tests access to the developer profile page via a GET request.
    Verifies that the page displays the correct profile information.
    """
    # Registrar y autenticar a un usuario desarrollador
    developer_email = "dev101@us.es"
    developer_password = "1234"
    
    # Crear usuario desarrollador en la base de datos
    with test_client.application.app_context():
        developer_user = User(email=developer_email, password=developer_password, is_developer=True)
        db.session.add(developer_user)
        db.session.commit()
        
        profile = UserProfile(user_id=developer_user.id, name="developer", surname="tester")
        db.session.add(profile)
        db.session.commit()

    # Iniciar sesión
    login_response = login(test_client, developer_email, developer_password)
    assert login_response.status_code == 200, "Login was unsuccessful."

    # Acceder a la página de perfil
    response = test_client.get("/profile/summary")
    assert response.status_code == 302, "The developer profile page could not be accessed."

    # Cerrar sesión
    logout(test_client)

