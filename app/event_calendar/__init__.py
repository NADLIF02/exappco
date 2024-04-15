from flask import Blueprint
from .views import new_leave, view_calendar

bp = Blueprint('event_calendar', __name__, url_prefix='/event_calendar')
bp.add_url_rule('/new', view_func=new_leave, methods=['GET', 'POST'])
bp.add_url_rule('/view', view_func=view_calendar, methods=['GET'])
