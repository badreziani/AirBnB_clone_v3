#!/usr/bin/python3
""" script index.py"""

from flask import jsonify
from models import storage
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from api.v1.views import app_views

classes = {"amenity": Amenity, "city": City,
           "place": Place, "review": Review, "state": State, "user": User}


@app_views.route('/status')
def status():
    """ route that return status """
    return jsonify({'status': 'OK'})


@app_views.route('/stats')
def stats():
    """ length of resources """
    r_dict = {}

    for cls_name, cls in classes.items():
        r_dict[cls_name] = storage.count(cls)

    return jsonify(r_dict)
