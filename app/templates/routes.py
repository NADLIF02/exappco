# app/event_calendar/routes.py
from . import event_calendar  # Import Blueprint instance

@event_calendar.route('/')
def index():
    return "Event Calendar Home"
