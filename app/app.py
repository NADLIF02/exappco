from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        return render_template('calendar.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Ajouter la logique de vérification ici
        session['logged_in'] = True
        return redirect(url_for('home'))
    return render_template('auth/login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
