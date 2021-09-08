from app.model import lecturer
from app.model import student
from app.model.lecturer import Lecturer
from app.model.student import Student

from app import response, app, db
from flask import request

import math

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
        if not lecturer:
            return response_undefined_data()
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
def get_paginated_list(clss, url, start, limit):
    # ambil query dari tabel lecturer => class yang akan dibuat paginasi
    results = clss.query.all()
    #ubah format agar serialized
    print("==============")
    print(results)
    data = list(map(format_lecturer, results))
    #hitung semua isi value array
    count = len(data)

    obj = {}

    if (count < start):
        # obj['success'] = False
        # obj['message'] = "Page yang dipilih (start) melewati batas total data!"
        # return obj
        data = []
    # else:
        # make response
    obj['success'] = True
    obj['start_page'] = start
    obj['per_page'] = limit
    obj['total_data'] = count
    #ceil agar bilangan menjadi bulat ke atas
    obj['total_page'] = math.ceil(count / limit)
    # make URLs
    # make previous url
    if start == 1:
        obj['previous'] = ''
    else:
        #ambil nilai start yg paling tinggi nilainya
        start_copy = max(1, start - limit)
        #ambil nilai data yg hendak ditampilkan querynya di previous page 
        #misal kiat punya 5 data, dengan limit tampil adalah 2 per page
        #saat di posisi page ke 5 maka kita bisa set previous limit yg tampil adalah 5 -1 = 4
        limit_copy = start - 1
        obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
    # make next url
    #jika misal total data ada 5
    #kita set mulai dari page 2 dan limit 3
    #jumlah melebihi count maka nex = kosong
    if start + limit > count:
        obj['next'] = ''
    else:
        start_copy = start + limit
        obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
    # finally extract result hasil sesuai batasnya
    #slicing array dimana dimulai dari start - 1 + limit
    obj['data'] = data[(start - 1):(start - 1 + limit)]
    return obj

#buat fungsi paginate
def paginate():
    #ambil parameter get 
    #sample http://127.0.0.1:5000/api/lecturer/page?start=3&limit=4
    start = request.args.get('start', 1)
    limit = request.args.get('limit', 20)
    if(limit > 100): limit = 20
    try:
        #default display first page
        if start == None or limit == None:
            return response.success(get_paginated_list(
            Lecturer, 
            'http://127.0.0.1:5000/api/lecturer/page', 
            start=request.args.get('start',1), 
            limit=request.args.get('limit',5)
            ))
            #custom parameters
        else:
            return response.success(get_paginated_list(
            Lecturer, 
            'http://127.0.0.1:5000/api/lecturer/page', 
            start=int(start), 
            limit=int(limit)
            ))

    except Exception as e:
        return response.error(e)