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

"""SQLAlchemy model for a user visit."""

from datetime import datetime

from flask_template import db


class Visit(db.Model):
    """SQLAlchemy class to register user's IPv4."""
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(15))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
