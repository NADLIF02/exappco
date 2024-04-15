from flask import render_template, request, redirect, url_for, session, flash
from . import auth
from .forms import LoginForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        # Logique de vérification des identifiants ici
        # Supposons une vérification réussie :
        session['logged_in'] = True
        flash('You have been logged in.', 'success')
        return redirect(url_for('calendar.display'))
    return render_template('auth/login.html', form=form)
