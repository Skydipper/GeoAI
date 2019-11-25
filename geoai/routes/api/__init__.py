import datetime
from flask import jsonify, request


def error(status=500, detail='Generic Error'):
    """Generic Error"""
    error = {
        'status': status,
        'detail': detail
    }
    return jsonify(errors=[error]), status
