from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'votre_cle_secrete_ici'

# Identifiants de test
USERS = {
    "admin": "admin123",
    "user": "password"
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in USERS and USERS[username] == password:
            session['logged_in'] = True
            session['username'] = username
            flash('Vous êtes maintenant connecté!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Identifiant ou mot de passe incorrect!', 'error')
    return render_template('auth/login.html')
