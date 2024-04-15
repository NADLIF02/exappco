from flask import Blueprint, render_template, request, redirect, url_for, session

# Define the Blueprint
main = Blueprint('main', __name__)

# Home page route
@main.route('/')
def home():
    # Check if user is logged in
    if not session.get('logged_in'):
        # Redirect to login page if not logged in
        return redirect(url_for('main.login'))
    else:
        # Show the calendar page if logged in
        return render_template('event_calendar/calendar.html')

# Login page route
@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Here you should verify the username and password
        # For now, we just assume login is successful
        session['logged_in'] = True
        return redirect(url_for('main.home'))
    return render_template('auth/login.html')
