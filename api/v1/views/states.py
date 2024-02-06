#!/usr/bin/python3
"""Simple page to test api"""
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.state import State
from flask import request
from flask import abort


@app_views.route('/states', methods=['GET'])
def states():
    """Retrieves all states objects"""
    objects = storage.all(State)
    objects_lst = [v.to_dict() for k, v in objects.items()]
    return jsonify(objects_lst), 200


@app_views.route('/states/<state_id>', methods=['GET', 'PUT'])
def get_state(state_id):
    """Retrieves the class with given id"""
    state = storage.get("State", state_id)
    if not state:
        abort(404)

    if request.method == "POST":
        json_data = request.get_json(silent=True)
        if not json_data:
            return jsonify({'error': 'Not a JSON'}), 400
        json_data.pop('id', None)
        json_data.pop('created_at', None)
        json_data.pop('updated_at', None)
        state = State(**json_data)
        state.save()
        return jsonify(state.to_dict()), 200
    return jsonify(state.to_dict()), 201


@app_views.route('/states', methods=['POST'])
def create_state():
    """Add new state to storage"""
    json_data = request.get_json(silent=True)
    if json_data:
        name = json_data.get("name", None)
        if name:
            for state in storage.all(State).values():
                if state.name == name:
                    return jsonify(state.to_dict()), 201
            state = State()
            state.name = name
            state.save()
            return jsonify(state.to_dict()), 201
        return jsonify({'error': "Missing name"}), 400
    return jsonify({'error': "Not a JSON"}), 400
