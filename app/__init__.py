from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Create the SQLAlchemy object

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
    app.config['SECRET_KEY'] = 'your_secret_key'
    
    db.init_app(app)  # Initialize db with the Flask app

    from app.event_calendar import bp as calendar_bp
    app.register_blueprint(calendar_bp)

    return app
