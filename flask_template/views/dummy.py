# -*- coding: utf-8 -*-
#
# This file is part of Flask-Template.
# Copyright (C) 2018 Grzegorz Jacenków.
#
# Flask-Template is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Flask-Template is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

"""The list of blueprints for /dummy endpoint."""

from flask import Blueprint, abort, jsonify, request

from flask_template import db
from flask_template.models import Visit

# Register the endpoint "/dummy" as a blueprint.
blueprint = Blueprint(
    "dummy_blueprint",
    __name__,
    url_prefix="/dummy",
)


@blueprint.route("/", methods=["GET"])
def get_dummy():
    """Render a dummy response as JSON object."""
    return jsonify({
        "status": "ok"
    })


@blueprint.route("/visit/<int:id>/", methods=["GET"])
def get_visit(id):
    """Get the visit by its ID."""
    visit = Visit.query.get(id)

    return jsonify({
        "id": visit.id,
        "ip": visit.ip,
        "timestamp": visit.timestamp
    })


@blueprint.route("/visit/", methods=["GET"])
def get_visits():
    """Get all registered visits."""
    visits = []

    # Check for GET parameter "id".
    if request.args.get("id"):
        return jsonify({
            "id_passed": request.args.get("id"),
            "message": "Use /visit/id instead!"
        })

    for visit in Visit.query.all():
        visits.append({
            "id": visit.id,
            "ip": visit.ip,
            "timestamp": visit.timestamp
        })

    return jsonify(visits)


@blueprint.route("/register/", methods=["GET"])
def get_registered_visit():
    """Register visitor's IP address."""
    visitor_ip = request.remote_addr

    # Create an entry in the database.
    visit = Visit(ip=visitor_ip)
    db.session.add(visit)
    db.session.commit()

    return jsonify({
        "ip": visitor_ip
    })


@blueprint.route("/add_two", methods=["POST"])
def post_number_to_add():
    """Return given number in POST request incremented by two."""
    request_data = request.get_json()

    try:
        return jsonify(2 + int(request_data['number']))
    except KeyError:
        abort(400, "Include field number in your POST request!")
