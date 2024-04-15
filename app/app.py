from flask import render_template, redirect, url_for, session
from .event_calendar.forms import EventForm 
app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('auth.login'))
    form = EventForm()  # Créez une instance du formulaire
    return render_template('event_calendar/calendar.html', form=form)
    
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
