from flask import Blueprint

event_calendar = Blueprint('event_calendar', __name__)

# Import routes at the end of the file to avoid circular import issues
from . import routes
