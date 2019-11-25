"""MIDDLEWARE"""
from flask import request
from functools import wraps
import json
import logging
from geoai.routes.api import error


def get_mc_info(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.method == 'POST':
            data_array = request.get_json().get('timeseries')
            window = request.args.get('window', None)
            if window:
                window = int(window)
            mc_number = request.args.get('mc_number', None)
            if mc_number:
                mc_number = int(mc_number)
            bin_number = request.args.get('bin_number', None)
            if bin_number:
                bin_number = int(bin_number)
            if not data_array:
                return error(status=400, detail='[MC] Timeseries is required')
        kwargs["timeseries"] = data_array
        kwargs["window"] = window
        kwargs["mc_number"] = mc_number
        kwargs["bin_number"] = bin_number
        return func(*args, **kwargs)
    return wrapper
