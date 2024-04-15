# app/event_calendar/__init__.py
from flask import Blueprint

event_calendar = Blueprint('event_calendar', __name__)

from . import routes
