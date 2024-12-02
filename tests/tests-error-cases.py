def test_view_profile_not_logged_in(client):
    """Verifica que no se pueda acceder al perfil sin autenticación."""
    response = client.get('/profile/view')
    assert response.status_code == 403  # Acceso prohibido

def test_edit_profile_invalid_data(client, init_data):
    """Verifica que no se permita enviar datos inválidos al editar el perfil."""
    user, _ = init_data
    with client:
        # Simular usuario autenticado
        login_user(user)
        response = client.post('/profile/edit', data={
            'name': '',  # Nombre vacío
            'surname': '',  # Apellido vacío
        })
        assert response.status_code == 400
        assert b'Este campo es obligatorio' in response.data
