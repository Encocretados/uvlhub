import pytest

from app import create_app, db
from app.modules.auth.models import User


@pytest.fixture(scope="session")
def test_app():
    """Create and configure a new app instance for each test session."""
    test_app = create_app("testing")

    with test_app.app_context():
        # Imprimir los blueprints registrados
        print("TESTING SUITE (1): Blueprints registrados:", test_app.blueprints)
        yield test_app


@pytest.fixture(scope="module")
def test_user(test_app):
    """
    Crea un usuario de prueba en la base de datos y lo asegura en la sesión.
    """
    with test_app.app_context():
        from app.modules.auth.models import User

        # Crea un nuevo usuario
        user = User(email="user1@example.com", password="1234")

        # Añádelo a la sesión y guarda
        db.session.add(user)
        db.session.commit()

        # Asegúrate de que la instancia esté vinculada a la sesión
        db.session.flush()
        db.session.refresh(user)

        return user


@pytest.fixture(scope="module")
def test_client(test_app):

    with test_app.test_client() as testing_client:
        with test_app.app_context():
            print("TESTING SUITE (2): Blueprints registrados:", test_app.blueprints)

            db.drop_all()
            db.create_all()
            """
            The test suite always includes the following user in order to avoid repetition
            of its creation
            """
            user_test = User(email="test@example.com", password="test1234")
            db.session.add(user_test)
            db.session.commit()

            print("Rutas registradas:")
            for rule in test_app.url_map.iter_rules():
                print(rule)
            yield testing_client

            db.session.remove()
            db.drop_all()


@pytest.fixture(scope="function")
def clean_database():
    db.session.remove()
    db.drop_all()
    db.create_all()
    yield
    db.session.remove()
    db.drop_all()
    db.create_all()


def login(test_client, email, password):
    """
    Authenticates the user with the credentials provided.

    Args:
        test_client: Flask test client.
        email (str): User's email address.
        password (str): User's password.

    Returns:
        response: POST login request response.
    """
    response = test_client.post(
        "/login", data=dict(email=email, password=password), follow_redirects=True
    )
    return response


def logout(test_client):
    """
    Logs out the user.

    Args:
        test_client: Flask test client.

    Returns:
        response: Response to GET request to log out.
    """
    return test_client.get("/logout", follow_redirects=True)


def validates_email(test_client, email, password, key):
    """
    Authenticates the user with the credentials provided.

    Args:
        test_client: Flask test client.
        key (int): key recieved in the user's email.

    Returns:
        response: POST login request response.
    """
    response = test_client.post(
        "/email_validation",
        data=dict(email=email, password=password, key=key),
        follow_redirects=True,
    )
    return response
