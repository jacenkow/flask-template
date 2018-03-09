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

"""Collection of blueprints for the project."""

from flask_template.views.dummy import blueprint as dummy_blueprint
from flask_template.views.main import blueprint as main_blueprint

blueprints = [
    dummy_blueprint,
    main_blueprint,
]
