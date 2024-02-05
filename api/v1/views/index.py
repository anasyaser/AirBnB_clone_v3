#!/usr/bin/python3
"""Simple page to test api"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def status():
    """Return the status"""
    return jsonify({"status": "OK"}), 200
