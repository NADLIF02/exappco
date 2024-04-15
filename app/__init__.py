from flask import Flask
from .event_calendar import bp as event_calendar_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.register_blueprint(event_calendar_bp)
    return app
