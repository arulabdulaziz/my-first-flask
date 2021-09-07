from app import app
from app.controller import LecturerController, UserController
from flask import request, make_response, jsonify, json
from app.validation.lecturer import schema as lecturer_schema_validation
from app.validation.user import schema_login, schema_register
from flask_expects_json import expects_json
from app.error_handler import bad_request, unauthorization
from flask_jwt_extended import get_jwt_identity, jwt_required, get_jwt
from werkzeug.exceptions import HTTPException
@app.route("/")
def index():
    return "Hello World Flask"

@app.route("/register", methods=["POST"])
@expects_json(schema_register)
def register():
    return UserController.register()
@app.route("/login", methods=["POST"])
@expects_json(schema_login)
def login():
    return UserController.login()


@app.route("/lecturer", methods=["GET", "POST"])
@jwt_required(lambda a: a)
@expects_json(lecturer_schema_validation, ignore_for=['GET'])
def lecturers():
    current_user = get_jwt_identity()
    if not current_user:
        return unauthorization(current_user)
    if request.method == "POST":
        return LecturerController.create()
    return LecturerController.index()

    
@app.route("/lecturer/<id>", methods=["GET", "PUT", "DELETE"])
@jwt_required(lambda a: a)
@expects_json(lecturer_schema_validation, ignore_for=['GET', "DELETE"])
def lecturer(id):
    current_user = get_jwt_identity()
    if not current_user:
        return unauthorization(current_user)
    if request.method == "PUT":
        return LecturerController.update(id)
    elif request.method == "DELETE":
        return LecturerController.destroy(id)
    return LecturerController.show(id)


@app.errorhandler(400)
def bad_request_400(error):
    return bad_request(error)
@app.errorhandler(422)
def error_422(error):
    return unauthorization(error)
@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response
