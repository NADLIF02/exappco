from flask import Flask, render_template, request, redirect, url_for, session
from app.event_calendar.forms import EventForm  # Adjusted import to correctly reference the module

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'

    from app.auth.views import auth_bp  # Assuming your auth views are structured in a Blueprint
    app.register_blueprint(auth_bp, url_prefix='/auth')

    @app.route('/')
    def home():
        if not session.get('logged_in'):
            return redirect(url_for('auth.login'))
        form = EventForm()  # Create an instance of the form
        return render_template('event_calendar/calendar.html', form=form)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            # Verification logic here
            session['logged_in'] = True
            return redirect(url_for('home'))
        return render_template('auth/login.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True)
