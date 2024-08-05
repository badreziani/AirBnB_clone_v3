#!/usr/bin/python3
""" script to create Blueprint app_views"""

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix="/api/v1")

# imports that ensure routes are registerd with app_views bp
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views import users
