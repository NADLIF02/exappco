from flask import Blueprint

event_calendar = Blueprint('event_calendar', __name__)

from . import routes
