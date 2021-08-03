from app.api import bp
from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES

def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response

def page_not_found(message):
    return error_response(404,message)


def internal_server_error(message):
    return error_response(500,message)

def errormessage(errormessage):
    message ={
        'error':errormessage
    }
    return jsonify(message)
def successmessage(successinfo):
    mesaage ={
        'message':successinfo
    }
    return jsonify(mesaage)