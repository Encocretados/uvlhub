import pytest
from app import create_app, db
from app.modules.auth.models import User
from app.modules.profile.models import UserProfile

@pytest.fixture
def app():
    """Configura el entorno de pruebas con una base de datos en memoria."""
    app = create_app('testing')  # Configuración para pruebas
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Base de datos en memoria
    app.config['TESTING'] = True

    with app.app_context():
        db.create_all()  # Crea las tablas necesarias
        yield app
        db.session.remove()
        db.drop_all()  # Limpia después de las pruebas

@pytest.fixture
def client(app):
    """Retorna un cliente de pruebas para realizar peticiones HTTP."""
    return app.test_client()

@pytest.fixture
def init_data():
    """Crea datos iniciales para pruebas."""
    user = User(email='test@example.com', password='hashed_password')
    user_profile = UserProfile(
        user=user,
        name='John',
        surname='Doe',
        orcid='0000-0001-2345-6789',
        affiliation='Test University'
    )
    db.session.add(user)
    db.session.add(user_profile)
    db.session.commit()
    return user, user_profile
