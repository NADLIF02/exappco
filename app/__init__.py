from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'votre_cle_secrete_ici'

    from .auth import auth as auth_blueprint
    from .calendar import calendar as calendar_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(calendar_blueprint, url_prefix='/calendar')

    return app
