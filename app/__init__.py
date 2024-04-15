from flask import Flask
from .auth import auth as auth_blueprint
from .event_calendar import event_calendar as calendar_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.default')  # Assuming you have a config directory with settings

    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(calendar_blueprint, url_prefix='/calendar')

    return app
