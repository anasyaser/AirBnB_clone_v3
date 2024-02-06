#!/usr/bin/python3
"""handle cities requests"""
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.state import State
from models.city import City
from flask import request
from flask import abort


@app_views.route('/states/<state_id>/cities', methods=['GET'])
def get_state_cities(state_id):
    """Retrieves all state cities objects"""
    object = storage.get("State", state_id)
    if not object:
        abort(404)
    cities = object.cities
    return jsonify([city.to_dict() for city in cities]), 200


@app_views.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    """Retrieves all state cities objects"""
    city = storage.get("City", city_id)
    if not object:
        abort(404)
    return jsonify(city.to_dict()), 200


# # @app_views.route('/states/<state_id>', methods=['GET', 'PUT'])
# def get_city(state_id):
#     """Retrieves the class with given id"""
#     state = storage.get("State", state_id)
#     if not state:
#         abort(404)

#     if request.method == "PUT":
#         json_data = request.get_json(silent=True)
#         if not json_data:
#             return jsonify({'error': 'Not a JSON'}), 400
#         json_data.pop('id', None)
#         json_data.pop('created_at', None)
#         json_data.pop('updated_at', None)
#         state = State(**json_data)
#         state.save()
#         return jsonify(state.to_dict()), 201
#     return jsonify(state.to_dict()), 201


# # @app_views.route('/states', methods=['POST'])
# def create_city():
#     """Add new state to storage"""
#     json_data = request.get_json(silent=True)
#     if json_data:
#         name = json_data.get("name", None)
#         if name:
#             for state in storage.all(State).values():
#                 if state.name == name:
#                     return jsonify(state.to_dict()), 201
#             state = State()
#             state.name = name
#             state.save()
#             return jsonify(state.to_dict()), 201
#         return jsonify({'error': "Missing name"}), 400
#     return jsonify({'error': "Not a JSON"}), 400
