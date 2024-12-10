import pytest
from app import db
from app.modules.auth.models import User
from app.modules.dataset.models import DataSet, DSMetaData, PublicationType, DatasetRating
from flask_login import login_user


@pytest.fixture(scope="module")
def test_client(test_client):
    """
    Creates a test client fixture to be used in the tests,
    and sets up the database with specific testing data.
    """
    with test_client.application.app_context():
        user_test = create_user(email="user_test@example.com", password="password123")
        dataset_test = create_dataset(user_id=user_test.id)

    yield test_client

    # Cleanup después de las pruebas
    with test_client.application.app_context():
        db.session.delete(dataset_test)
        db.session.delete(user_test)
        db.session.commit()


def create_user(email, password):
    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return user


def create_dataset(user_id):
    ds_meta_data = DSMetaData(
        title="Test Dataset",
        description="Test dataset description",
        publication_type=PublicationType.JOURNAL_ARTICLE,
    )
    db.session.add(ds_meta_data)
    db.session.commit()

    dataset = DataSet(user_id=user_id, ds_meta_data_id=ds_meta_data.id)
    db.session.add(dataset)
    db.session.commit()
    return dataset


def test_rate_dataset(test_client):
    with test_client.application.app_context():
        # Crear un usuario y dataset para el test
        user = create_user(email="test_user_rate@example.com", password="password123")
        dataset = create_dataset(user_id=user.id)

        # Iniciar sesión con el usuario
        login_user(user)

        # Realizar la solicitud para calificar el dataset
        response = test_client.post(
            f"/datasets/{dataset.id}/rate",
            json={"rating": 4},
            follow_redirects=True
        )

        # Verificar la respuesta
        assert response.status_code == 200, "La solicitud para calificar el dataset falló."
        data = response.get_json()
        assert data["status"] == "success", "La calificación no se registró correctamente."
        assert data["average_rating"] == 4.0, "La calificación promedio no es la esperada."
        assert data["total_ratings"] == 1, "El número total de calificaciones no es el esperado."

        # Verificar que la calificación se guardó en la base de datos
        rating = DatasetRating.query.filter_by(user_id=user.id, dataset_id=dataset.id).first()
        assert rating is not None, "La calificación no se guardó en la base de datos."
        assert rating.rating == 4, "El valor de la calificación no es el esperado."

        # Eliminar los datos de prueba
        db.session.delete(rating)
        db.session.delete(dataset)
        db.session.delete(user)
        db.session.commit()
