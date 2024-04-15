from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .event_calendar import event_calendar as calendar_blueprint
    app.register_blueprint(calendar_blueprint, url_prefix='/calendar')

    # Import routes after the blueprint registration
    from .event_calendar import routes  # This import is deferred until after the Blueprint is registered

    return app
