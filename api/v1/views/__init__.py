#!/usr/bin/python3
""" script to create Blueprint app_views"""

from flask import Blueprint

app_views = Blueprint('app_views', __name__)

# import that ensure routes are registerd with app_views bp
from api.v1.views import index


