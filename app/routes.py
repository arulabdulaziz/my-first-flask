from app import app
from app.controller import LecturerController
from flask import request, make_response, jsonify
from app.validation.lecturer import schema as lecturer_schema_validation
from flask_expects_json import expects_json
from app.error_handler import bad_request
@app.route("/")
def index():
    return "Hello World Flask"
@app.route("/lecturer", methods=["GET", "POST"])
@expects_json(lecturer_schema_validation, ignore_for=['GET'])
def lecturers():
    if request.method == "POST":
        return LecturerController.create()
    return LecturerController.index()
@app.route("/lecturer/<id>", methods=["GET", "PUT", "DELETE"])
@expects_json(lecturer_schema_validation, ignore_for=['GET', "DELETE"])
def lecturer(id):
    if request.method == "PUT":
        return LecturerController.update(id)
    elif request.method == "DELETE":
        return LecturerController.destroy(id)
    return LecturerController.show(id)
@app.errorhandler(400)
def bad_request_400(error):
    return bad_request(error)
