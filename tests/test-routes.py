from flask_login import login_user
from app.modules.auth.models import User
from app.modules.profile.models import UserProfile

def test_view_profile(client, init_data):
    """Verifica que se puede visualizar el perfil de un usuario."""
    user, _ = init_data
    with client:
        response = client.get('/profile/view')
        assert response.status_code == 200
        assert b'John Doe' in response.data
        assert b'Test University' in response.data

def test_edit_profile_get(client, init_data):
    """Verifica que la ruta de edición del perfil devuelve el formulario."""
    user, _ = init_data
    with client:
        # Simular usuario autenticado
        login_user(user)
        response = client.get('/profile/edit')
        assert response.status_code == 200
        assert b'Editar Perfil' in response.data

def test_edit_profile_post(client, init_data):
    """Verifica que se pueda actualizar el perfil de un usuario."""
    user, _ = init_data
    with client:
        # Simular usuario autenticado
        login_user(user)
        response = client.post('/profile/edit', data={
            'name': 'Jane',
            'surname': 'Smith',
            'orcid': '0000-0002-9876-5432',
            'affiliation': 'New University'
        }, follow_redirects=True)
        
        assert response.status_code == 200
        assert 'Perfil actualizado con éxito' in response.data
        
        # Verificar cambios en la base de datos
        updated_profile = UserProfile.query.filter_by(user_id=user.id).first()
        assert updated_profile.name == 'Jane'
        assert updated_profile.surname == 'Smith'
