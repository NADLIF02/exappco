from . import event_calendar

@event_calendar.route('/')
def index():
    return "Welcome to the Event Calendar!"
