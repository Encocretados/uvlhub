from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from .services import obtener_respuesta_ia

# Crear el Blueprint para la IA
ia_bp = Blueprint('ia', __name__, template_folder='templates', static_folder='assets')

@ia_bp.route('/ia', methods=['GET', 'POST'])
def ia_page():
    response = None
    if request.method == 'POST':
        # Obtener la pregunta enviada por el usuario desde el formulario
        user_query = request.form.get('user_query')
        if user_query:
            # Llamar a la función para obtener la respuesta de la IA
            response = obtener_respuesta_ia(user_query)
    return render_template('ia.html', response=response)
    