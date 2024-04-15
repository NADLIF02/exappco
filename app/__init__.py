from flask import Flask
from .event_calendar import event_calendar
from .auth import auth

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    app.register_blueprint(auth)
    app.register_blueprint(event_calendar)

    return app
