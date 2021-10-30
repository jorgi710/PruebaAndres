# -*- coding: utf-8 -*-
#########################################################
from flask import Blueprint

api = Blueprint('api', __name__)

from. import errors
from.v1.example import example_routes


@api.before_request
def before_request():
    pass


@api.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

