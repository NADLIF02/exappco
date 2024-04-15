from flask import Blueprint, render_template, request, redirect, url_for, session, flash

auth = Blueprint('auth', __name__)

USERS = {
    "admin": "admin123",
    "user": "password"
}

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in USERS and USERS[username] == password:
            session['logged_in'] = True
            session['username'] = username
            flash('Vous êtes maintenant connecté!', 'success')
            return redirect(url_for('calendar.display'))
        else:
            flash('Identifiant ou mot de passe incorrect!', 'error')
    return render_template('auth/login.html')
