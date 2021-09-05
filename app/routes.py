from app import app
from app.controller import LecturerController

@app.route("/")
def index():
    return "Hello World Flask"
@app.route("/lecturer", methods=["GET"])
def lecturers():
    return LecturerController.index()