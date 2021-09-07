from jsonschema import ValidationError
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
def unauthorization(error):
    return error_response(["You must Login first"], 401)