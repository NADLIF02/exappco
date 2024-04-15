from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
    db.init_app(app)

    from app.event_calendar.views import bp as calendar_bp
    app.register_blueprint(calendar_bp)

    return app
