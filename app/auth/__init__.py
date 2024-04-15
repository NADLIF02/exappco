from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import routes  # Relative import of routes within the same Blueprint package
