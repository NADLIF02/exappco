from flask import render_template, current_app
from . import auth

@auth.route('/login', methods=['GET', 'POST'])
def login():
    current_app.logger.info("Accessing the login route")
    return render_template('auth/login.html')
