from flask import Blueprint

auth = Blueprint('auth', __name__)

import app.auth.routes
