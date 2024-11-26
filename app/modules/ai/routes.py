# routes.py
from flask import Blueprint, request, jsonify
from .services import AIService

ai_bp = Blueprint('ai', __name__)
service = AIService()

@ai_bp.route('/ai/process', methods=['POST'])
def process_query():
    query = request.json.get('query', '')
    response = service.process_query(query)
    return jsonify({'response': response})
