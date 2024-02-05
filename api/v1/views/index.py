#!/usr/bin/python3
"""Simple page to test api"""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def status():
    """Return the status"""
    return jsonify({"status": "OK"}), 200


@app_views.route('stats')
def get_stats():
    """Retrieves the number of each objects"""
    stats = {
        "amenities": "Amenity",
        "cities": "City",
        "places": "Place",
        "reviews": "Review",
        "states": "State",
        "users": "User"
    }
    return jsonify({name: storage.count(cls) for name, cls in stats.items()})
