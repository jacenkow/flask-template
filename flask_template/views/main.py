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

"""The list of blueprints for / endpoint."""

from flask import Blueprint, render_template


# Register the main endpoint "/" as a blueprint.
blueprint = Blueprint(
    "main_blueprint",
    __name__,
    url_prefix="/",
)


@blueprint.route("/", methods=["GET"])
def get_home():
    """Render the main page."""
    return render_template("main.html")
