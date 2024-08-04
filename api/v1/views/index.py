#!/usr/bin/python3
""" script index.py"""

from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status')
def status():
    """ route that return status """
    return jsonify({'status': 'OK'})
