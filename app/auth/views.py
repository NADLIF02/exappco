from flask import render_template, request, redirect, url_for, session
from . import auth

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Logique de vérification des identifiants
        session['logged_in'] = True
        return redirect(url_for('calendar.display'))
    return render_template('auth/login.html')
