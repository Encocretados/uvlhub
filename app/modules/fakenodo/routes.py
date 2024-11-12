from flask import jsonify, make_response
from app.modules.fakenodo import fakenodo_bp

base_url = "/fakenodo/api"


@fakenodo_bp.route(base_url, methods=["GET"])
def test_connection_fakenodo():
    response = {"status": "success", "message": "The API of Fakenodo connected successfully"}
    return jsonify(response)


@fakenodo_bp.route(base_url, methods=["POST"])
def create_fakenodo():
    response = {"status": "success", "message": "The deposition of Fakenodo was created"}
    return make_response(jsonify(response), 201)


@fakenodo_bp.route(base_url + "/<id>/deposition", methods=["POST"])
def deposition_files_fakenodo(id):
    response = {
        "status": "success",
        "message": f"The deposition {id} was successfully created",
    }
    return make_response(jsonify(response), 201)


@fakenodo_bp.route(base_url + "/<id>", methods=["DELETE"])
def delete_deposition_fakenodo(id):
    response = {
        "status": "success",
        "message": f"The deposition {id} was succesfully deleted",
    }
    return make_response(jsonify(response), 200)


@fakenodo_bp.route(base_url + "/<id>/resources/submit", methods=["POST"])
def publish_deposition_fakenodo(id):
    response = {
        "status": "success",
        "message": f"Deposition with ID {id} succesfully published in the API of Fakenodo",
    }
    return make_response(jsonify(response), 202)


@fakenodo_bp.route(base_url + "/<id>", methods=["GET"])
def get_deposition_fakenodo(id):
    response = {
        "status": "success",
        "message": f"The deposition with ID {id} successfully gotten in the API of Fakenodo",
        "doi": "10.5072/fakenodo.123456",
    }
    return make_response(jsonify(response), 200)
