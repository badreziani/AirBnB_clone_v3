#!/usr/bin/python3
""" script for State view """

from models import storage
from models.state import State
from api.v1.views import app_views
from flask import jsonify, abort
from flask import request, make_response


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_all_states():
    """Route that returns all states"""
    all_list = []
    state_dict = storage.all(State)
    for _, obj in state_dict.items():
        all_list.append(obj.to_dict())

    return make_response(jsonify(all_list), 200)


@app_views.route('/states/<string:state_id>', methods=['GET'], strict_slashes=False)
def get_state_by_id(state_id):
    """Route that returns a state by its ID"""
    stat_obj = storage.get(State, state_id)
    if not stat_obj:
        abort(404)

    return make_response(jsonify(stat_obj.to_dict()), 200)


@app_views.route('/states/<string:state_id>', methods=['DELETE'],
                 strict_slashes=False)
def state_delete(state_id):
    """ delete http request"""
    stat_obj = storage.get(State, state_id)
    if not stat_obj:
        abort(404)
    storage.delete(stat_obj)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def state_post():
    """post http request """
    req_json = request.get_json()
    if not req_json:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'name' not in req_json:
        return make_response(jsonify({'error': 'Missing name'}), 400)

    obj = State()

    for k, v in req_json.items():
        setattr(obj, k, v)

    # add obj to current DB session and save it.
    storage.new(obj)
    storage.save()
    new_state = obj.to_dict()
    return make_response(jsonify(new_state), 201)


@app_views.route('/states/<string:state_id>', methods=['PUT'], strict_slashes=False)
def state_update(state_id):
    """put http request"""
    stat_obj = storage.get(State, state_id)
    if not stat_obj:
        abort(404)

    req_json = request.get_json()
    if not req_json:
        return make_resonse(jsonify({'error': 'Not a JSON'}), 400)

    ignore_keys = {'id', 'created_at', 'updated_at'}
    for k, v in req_json.items():
        if k not in ignore_keys:
            setattr(stat_obj, k, v)

    storage.save()
    return make_response(jsonify(stat_obj.to_dict()), 200)
