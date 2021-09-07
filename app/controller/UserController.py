import datetime
from app.model.user  import User

from app import response, app, db
from flask import request
from flask_jwt_extended import *

def format_user(obj):
    return {
        "id": obj.id,
        "name": obj.name,
        "email": obj.email,
        "level": obj.level,
        "created_at": obj.created_at,
        "updated_at": obj.updated_at,
    }
def response_already_exist_email():
    return response.error([{"message": "Email Already Exist"}], 400)
def response_invalid_email_or_password():
    return response.error([{"message": "Invalid Email or Password"}], 400)
def register():
    try:
        # https://medium.com/analytics-vidhya/server-validation-in-flask-api-with-json-schema-963aa05e305f   <- validation input json
        # nidn = request.args.get('nidn') # to get params in json
        email = request.json["email"] # to get body in json
        name = request.json["name"]
        password = request.json["password"]
        data = User.query.filter_by(email = email).first()
        if data:
            return response_already_exist_email()
        level = 1
        user = User(email = email, name = name, level = level)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return response.success(format_user(user), 201)
    except Exception as e:
        return response.error(e)

def login():
    try:
        # https://medium.com/analytics-vidhya/server-validation-in-flask-api-with-json-schema-963aa05e305f   <- validation input json
        # nidn = request.args.get('nidn') # to get params in json
        email = request.json["email"] # to get body in json
        password = request.json["password"]
        user = User.query.filter_by(email = email).first()
        if not user:
            return response_invalid_email_or_password()
        elif not user.check_password(password):
            return response_invalid_email_or_password()
        expires = datetime.timedelta(days=7)
        expires_refresh = datetime.timedelta(days=7)
        result = format_user(user)
        access_token = create_access_token(result, fresh=True, expires_delta=expires)
        refresh_token = create_refresh_token(result, expires_delta=expires_refresh)
        result["access_token"] =  access_token
        result["refresh_token"] =  refresh_token
        return response.success(result)
    except Exception as e:
        return response.error(e)