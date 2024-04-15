from flask import Blueprint

# Create a Blueprint object
event_calendar = Blueprint('event_calendar', __name__)

# Routes are imported after the blueprint creation but before the blueprint registration
from . import routes
