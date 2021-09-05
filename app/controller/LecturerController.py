from app.model import lecturer
from app.model.lecturer import Lecturer

from app import response, app, db
from flask import request
def formatLecturer(data):
    return {
        "id": data.id,
        "name": data.name,
        "nidn": data.nidn,
        "phone": data.phone,
        "address": data.address,
        "created_at": data.created_at,
        "updated_at": data.updated_at,
    }

def index():
    try:
        lecturer = Lecturer.query.all()
        return response.success(list(map(formatLecturer, lecturer)))
    except Exception as e:
        return response.error(e)