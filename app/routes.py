from app import app
from app.controller import LecturerController
from flask import request

@app.route("/")
def index():
    return "Hello World Flask"
@app.route("/lecturer", methods=["GET", "POST"])
def lecturers():
    if request.method == "POST":
        return LecturerController.create()
    return LecturerController.index()
@app.route("/lecturer/<id>", methods=["GET"])
def lecturer(id):
    return LecturerController.show(id)
