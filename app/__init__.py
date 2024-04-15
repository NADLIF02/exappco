# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from app.event_calendar import event_calendar as calendar_blueprint
    app.register_blueprint(calendar_blueprint, url_prefix='/calendar')

    return app
