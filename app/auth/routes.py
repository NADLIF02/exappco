from flask import render_template, redirect, url_for, request, flash, session
from . import auth  # Importing the Blueprint instance from the __init__.py within the same auth directory

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Here you should verify the username and password with your user model/database
        # This is just a placeholder logic
        if username == "admin" and password == "secret":
            session['logged_in'] = True
            flash('You were successfully logged in', 'success')
            return redirect(url_for('main.home'))  # Ensure 'main.home' is correctly defined in your routes
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('auth/login.html')

@auth.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out', 'info')
    return redirect(url_for('main.home'))  # Adjust the redirect as necessary
