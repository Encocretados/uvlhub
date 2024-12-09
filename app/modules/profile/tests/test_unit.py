import pytest
import time

from app import db
from app.modules.conftest import login, logout, validates_email
from app.modules.auth.models import User
from app.modules.profile.models import UserProfile
from app.modules.auth.services import AuthenticationService

authentication_service = AuthenticationService()


@pytest.fixture(scope="module")
def test_client(test_client):
    """
    Extends the test_client fixture to add additional specific data for module testing.
    for module testing (por example, new users)
    """
    with test_client.application.app_context():
        user_test = User(email='uvlhub.reply@gmail.com', password='uvlhub1234')
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
    login_response = login(test_client, "uvlhub.reply@gmail.com", "uvlhub1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    time.sleep(5)
    email = "uvlhub.reply@gmail.com"
    password = "uvlhub1234"
    clave = authentication_service.get_validation_email_key()
    validation_response = validates_email(test_client, email, password, clave)
    assert validation_response.status_code == 200, "Email key validation unsuccessful"

    response = test_client.get("/profile/edit")
    assert response.status_code == 200, "The profile editing page could not be accessed."
    assert b"Edit profile" in response.data, "The expected content is not present on the page"

    logout(test_client)
