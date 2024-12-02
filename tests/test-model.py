from app.modules.profile.models import UserProfile
from app.modules.auth.models import User

def test_user_creation(init_data):
    """Verifica que un usuario puede ser creado correctamente."""
    user, user_profile = init_data
    assert user.email == 'test@example.com'
    assert user_profile.name == 'John'
    assert user_profile.surname == 'Doe'

def test_user_profile_relationship(init_data):
    """Verifica que la relación entre User y UserProfile funciona."""
    user, user_profile = init_data
    assert user.profile.name == 'John'
    assert user_profile.user.email == 'test@example.com'
