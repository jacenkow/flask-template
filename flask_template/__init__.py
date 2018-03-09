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

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Setup Flask application.
app = Flask(__name__)
app.config.from_object("flask_template.config")

# Setup SQLAlchemy instance.
db = SQLAlchemy(app)

@app.before_first_request
def create_db():
    """Create the database if doesn't exist."""
    db.create_all()

# Register blueprints.
from flask_template.views import blueprints

for blueprint in blueprints:
    app.register_blueprint(blueprint)
