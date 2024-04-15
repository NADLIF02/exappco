from flask import Blueprint

event_calendar = Blueprint('event_calendar', __name__)

# Do not import routes here to avoid circular import
