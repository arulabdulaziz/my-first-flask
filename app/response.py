from flask import jsonify, make_response

def success(data, status = 200):
    res = {
        "success": True,
        "data": data,
    }
    return make_response(jsonify(res), status)

def error(error, status=400):
    res = {
        "success": False,
        "error": error,
    }
    return make_response(jsonify(res))
