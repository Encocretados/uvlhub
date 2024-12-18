import time

import pytest
from flask import url_for

from app import db
from app.modules.auth.models import User
from app.modules.auth.repositories import UserRepository
from app.modules.auth.services import AuthenticationService
from app.modules.profile.models import UserProfile
from app.modules.profile.repositories import UserProfileRepository

authentication_service = AuthenticationService()


@pytest.fixture(scope="module")
def test_client(test_client):
    """
    Extends the test_client fixture to add additional specific data for module testing.
    """
    with test_client.application.app_context():
        # Add HERE new elements to the database that you want to exist in the test context.
        # DO NOT FORGET to use db.session.add(<element>) and db.session.commit() to save the data.
        user_test = User(email="user1@example.com", password="1234", is_developer=False)
        db.session.add(user_test)
        db.session.commit()
        user2_test = User(
            email="uvlhub.reply@gmail.com", password="uvl12hub34", is_developer=False
        )
        db.session.add(user2_test)
        db.session.commit()

        profile = UserProfile(user_id=user_test.id, name="Name", surname="Surname")
        db.session.add(profile)
        db.session.commit()

    yield test_client


def test_login_and_email_authentification_success(test_client):
    response = test_client.post(
        "/login",
        data=dict(email="uvlhub.reply@gmail.com", password="uvl12hub34"),
        follow_redirects=True,
    )
    assert response.request.path == url_for(
        "auth.email_validation"
    ), "Login was unsuccessful"

    time.sleep(2)
    clave = authentication_service.get_validation_email_key()
    response = test_client.post(
        "/email_validation",
        data=dict(
            email="uvlhub.reply@gmail.com",
            password="uvl12hub34",
            key=clave,
        ),
        follow_redirects=True,
    )
    assert response.request.path == url_for(
        "public.index"
    ), "Email authetification was unsuccessful"
    test_client.get("/logout", follow_redirects=True)


def test_login_succes_but_email_authentification_unsuccessful(test_client):
    response = test_client.post(
        "/login",
        data=dict(email="uvlhub.reply@gmail.com", password="uvl12hub34"),
        follow_redirects=True,
    )
    assert response.request.path == url_for(
        "auth.email_validation"
    ), "Login was unsuccessful"

    time.sleep(2)
    clave = int(authentication_service.get_validation_email_key())
    if clave != 999999:
        clave += 1
    else:
        clave -= 1
    response = test_client.post(
        "/email_validation",
        data=dict(
            email="uvlhub.reply@gmail.com",
            password="uvl12hub34",
            key=str(clave),
        ),
        follow_redirects=True,
    )
    assert response.request.path == url_for(
        "auth.email_validation"
    ), "Email authetification was unexpectedly successful"
    assert "The key does not match".encode("utf-8") in response.data

    test_client.get("/logout", follow_redirects=True)


def test_login_success(test_client):
    response = test_client.post(
        "/login",
        data=dict(email="user1@example.com", password="1234"),
        follow_redirects=True,
    )

    assert response.request.path != url_for("auth.login"), "Login was unsuccessful"

    test_client.get("/logout", follow_redirects=True)


def test_correct_redirection_to_email_validation(test_client):
    response = test_client.post(
        "/login",
        data=dict(email="user1@example.com", password="1234"),
        follow_redirects=True,
    )

    assert response.request.path == url_for(
        "auth.email_validation"
    ), "Login was unsuccessful"
    test_client.get("/logout", follow_redirects=True)


def test_login_unsuccessful_bad_email(test_client):
    response = test_client.post(
        "/login",
        data=dict(email="bademail@example.com", password="Test1234#"),
        follow_redirects=True,
    )

    assert response.request.path == url_for("auth.login"), "Login was unsuccessful"
    test_client.get("/logout", follow_redirects=True)


def test_login_unsuccessful_bad_password(test_client):
    response = test_client.post(
        "/login",
        data=dict(email="user1@example.com", password="Basspassword"),
        follow_redirects=True,
    )

    assert response.request.path == url_for("auth.login"), "Login was unsuccessful"

    test_client.get("/logout", follow_redirects=True)


def test_signup_user_no_name(test_client):
    response = test_client.post(
        "/signup",
        data=dict(surname="Foo", email="test@example.com", password="Test1234#"),
        follow_redirects=True,
    )
    assert response.request.path == url_for(
        "auth.show_signup_form"
    ), "Signup was unsuccessful"
    assert b"This field is required" in response.data, response.data


def test_signup_user_unsuccessful(test_client):
    email = "test@example.com"
    response = test_client.post(
        "/signup",
        data=dict(name="Test", surname="Foo", email=email, password="Test1234#"),
        follow_redirects=True,
    )
    assert response.request.path == url_for(
        "auth.show_signup_form"
    ), "Signup was unsuccessful"
    assert f"Email {email} in use".encode("utf-8") in response.data


def test_signup_user_unsuccessful_password_without_uppercase_nor_lowercase(test_client):
    email = "test@example.com"
    response = test_client.post(
        "/signup",
        data=dict(name="Test", surname="Foo", email=email, password="1234#"),
        follow_redirects=True,
    )
    assert response.request.path == url_for(
        "auth.show_signup_form"
    ), "Signup was unsuccessful"
    assert (
        "Password must contain at least one uppercase letter".encode("utf-8")
        in response.data
    )
    assert (
        "Password must contain at least one lowercase letter".encode("utf-8")
        in response.data
    )


def test_signup_user_unsuccessful_password_without_numbers_nor_special_characters(
    test_client,
):
    email = "test@example.com"
    response = test_client.post(
        "/signup",
        data=dict(name="Test", surname="Foo", email=email, password="Test"),
        follow_redirects=True,
    )
    assert response.request.path == url_for(
        "auth.show_signup_form"
    ), "Signup was unsuccessful"
    assert "Password must contain at least one digit".encode("utf-8") in response.data
    assert (
        "Password must contain at least one special character: #,@,~,€".encode("utf-8")
        in response.data
    )


def test_signup_user_successful(test_client):
    response = test_client.post(
        "/signup",
        data=dict(
            name="Foo", surname="Example", email="foo@example.com", password="Foo1234#"
        ),
        follow_redirects=True,
    )
    # Ahora después de un login exitoso se pasa a la pestaña de verificacion del email
    assert response.request.path == url_for(
        "auth.email_validation"
    ), "Signup was unsuccessful"


def test_service_create_with_profie_success(clean_database):
    data = {
        "name": "Test",
        "surname": "Foo",
        "email": "service_test@example.com",
        "password": "Test1234#",
    }

    AuthenticationService().create_with_profile(**data)

    assert UserRepository().count() == 1
    assert UserProfileRepository().count() == 1


def test_service_create_with_profile_fail_no_email(clean_database):
    data = {"name": "Test", "surname": "Foo", "email": "", "password": "Test1234#"}

    with pytest.raises(ValueError, match="Email is required."):
        AuthenticationService().create_with_profile(**data)

    assert UserRepository().count() == 0
    assert UserProfileRepository().count() == 0


def test_service_create_with_profile_fail_no_password(clean_database):
    data = {
        "name": "Test",
        "surname": "Foo",
        "email": "test@example.com",
        "password": "",
    }

    with pytest.raises(ValueError, match="Password is required."):
        AuthenticationService().create_with_profile(**data)

    assert UserRepository().count() == 0
    assert UserProfileRepository().count() == 0


def test_signup_developer_unsuccessful_password_without_uppercase_nor_numbers(
    test_client,
):
    email = "test@example.com"
    response = test_client.post(
        "/signup/developer",
        data=dict(
            name="Dev",
            surname="Test",
            email=email,
            password="password#",
            team="University of Malaga",
            github="duplicategithub",
        ),
        follow_redirects=True,
    )

    assert response.request.path == url_for(
        "auth.show_developer_signup_form"
    ), "Signup was unsuccessful"
    assert (
        "Password must contain at least one uppercase letter".encode("utf-8")
        in response.data
    )
    assert "Password must contain at least one digit".encode("utf-8") in response.data


def test_signup_developer_unsuccessful_password_without_lowercase_nor_special_characters(
    test_client,
):
    email = "test@example.com"
    response = test_client.post(
        "/signup/developer",
        data=dict(
            name="Dev",
            surname="Test",
            email=email,
            password="PASSWORD123",
            team="University of Malaga",
            github="duplicategithub",
        ),
        follow_redirects=True,
    )

    assert response.request.path == url_for(
        "auth.show_developer_signup_form"
    ), "Signup was unsuccessful"
    assert (
        "Password must contain at least one lowercase letter".encode("utf-8")
        in response.data
    )
    assert (
        "Password must contain at least one special character: #,@,~,€".encode("utf-8")
        in response.data
    )


def test_developer_singup_success(test_client):
    # Prueba el correcto registro de un developer
    response = test_client.post(
        "/signup/developer",
        data=dict(
            name="DeveloperName",
            surname="DeveloperSurname",
            email="developer@example.com",
            password="Securepassword123#",
            team="University of Seville",
            github="devgithubuser",
        ),
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert response.request.path == url_for("public.index"), "Signup was unsuccessful"


def test_developer_signup_duplicate_email(test_client):
    # Prueba el fallo de registro con email duplicado
    test_client.post(
        "/signup/developer",
        data=dict(
            name="Dev",
            surname="Test",
            email="duplicate@example.com",
            password="Password123#",
            team="University of Malaga",
            github="duplicategithub",
        ),
        follow_redirects=True,
    )

    response = test_client.post(
        "/signup/developer",
        data=dict(
            name="DevNew",
            surname="TestNew",
            email="duplicate@example.com",
            password="Newpassword123#",
            team="University of Malaga",
            github="newgithub",
        ),
        follow_redirects=True,
    )

    assert response.status_code == 200


def test_developer_login_success(test_client):
    # Prueba el login exitoso de un developer
    response = test_client.post(
        "/login",
        data=dict(email="developer@example.com", password="Securepassword123#"),
        follow_redirects=True,
    )

    assert response.status_code == 200
