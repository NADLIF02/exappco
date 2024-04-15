from flask import render_template
from . import calendar

@calendar.route('/calendar')
def display():
    if not session.get('logged_in'):
        return redirect(url_for('auth.login'))
    return render_template('calendar/calendar.html')
