#!/usr/bin/python3
"""Simple page to test api"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def status():
    """Return the status"""
    return jsonify({"status": "OK"}), 200

@app_views.route('stats')
def get_stats():
    """Retrieves the number of each objects"""
    stats = {
        "Amenity": "amenities",
        "City": "cities",
        "Place": "places",
        "Review": "reviews",
        "State": "states",
        "User": "users"
    }
    return jsonify({name: storage.count(cls) for cls, name in stats.items()})
