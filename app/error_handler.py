from jsonschema import ValidationError
from flask import make_response, jsonify
from app.response import error as error_response
def bad_request(error):
    if isinstance(error.description, ValidationError):
        original_error = error.description
        return error_response([{"message": original_error.message}], 400)
    # handle other "Bad Request"-errors
    error = {
        "success": False,
        "errors": error,
    }
    return error