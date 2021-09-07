from app.model import lecturer
from app.model import student
from app.model.lecturer import Lecturer
from app.model.student import Student

from app import response, app, db
from flask import request
def format_lecturer(data):
    return {
        "id": data.id,
        "name": data.name,
        "nidn": data.nidn,
        "phone": data.phone,
        "address": data.address,
        "created_at": data.created_at,
        "updated_at": data.updated_at,
    }
def format_student(data):
    return {
        "id": data.id,
        "nim": data.nim,
        "name": data.name,
        "phone": data.phone,
        "address": data.address,
        "created_at": data.created_at,
        "updated_at": data.updated_at,
    }
def response_undefined_data():
    return response.error([{"message": "Lecturer not Found"}], 404)
def index():
    try:
        lecturer = Lecturer.query.all()
        return response.success(list(map(format_lecturer, lecturer)), 200)
    except Exception as e:
        return response.error(e)
def show(id):
    try:
        lecturer = Lecturer.query.filter_by(id = id).first()
        student = Student.query.filter((Student.first_lecturer == id) | (Student.second_lecturer==id)).all()
        lecturer = format_lecturer(lecturer)
        lecturer["students"] = list(map(format_student, student))
        return response.success(lecturer)
    except Exception as e:
        return response.error(e)
def create():
    try:
        # https://medium.com/analytics-vidhya/server-validation-in-flask-api-with-json-schema-963aa05e305f   <- validation input json
        # nidn = request.args.get('nidn') # to get params in json
        nidn = request.json["nidn"] # to get body in json
        name = request.json["name"]
        phone = request.json["phone"]
        address = request.json["address"]
        lecturer = Lecturer(nidn = nidn, name = name, phone = phone, address = address)
        db.session.add(lecturer)
        db.session.commit()
        return response.success(format_lecturer(lecturer))
    except Exception as e:
        return response.error(e)

def update(id):
    try:
        # https://medium.com/analytics-vidhya/server-validation-in-flask-api-with-json-schema-963aa05e305f   <- validation input json
        # nidn = request.args.get('nidn') # to get params in json
        lecturer = Lecturer.query.filter_by(id = id).first()
        if not lecturer:
            return response_undefined_data()
        lecturer.nidn = request.json["nidn"]
        lecturer.name = request.json["name"]
        lecturer.phone = request.json["phone"]
        lecturer.address = request.json["address"]
        db.session.commit()
        return response.success(format_lecturer(lecturer))
    except Exception as e:
        return response.error(e)
def destroy(id):
    try:
        lecturer = Lecturer.query.filter_by(id = id).first()
        if not lecturer:
            return response_undefined_data()
        db.session.delete(lecturer)
        db.session.commit()
        return response.success(format_lecturer(lecturer))
    except Exception as e:
        return response.error(e)
        