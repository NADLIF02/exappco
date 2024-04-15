from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Import the blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # Import the event_calendar Blueprint and its routes beforehand
    from .event_calendar import event_calendar as calendar_blueprint
    from .event_calendar import routes  # Import routes before registering the blueprint
    app.register_blueprint(calendar_blueprint, url_prefix='/calendar')

    return app
