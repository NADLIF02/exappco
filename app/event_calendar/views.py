from flask import render_template, request, redirect, url_for, flash, session
from . import calendar
from .forms import EventForm
from datetime import datetime

@calendar.route('/event_calendar', methods=['GET', 'POST'])
def display():
    if not session.get('logged_in'):
        return redirect(url_for('auth.login'))
    form = EventForm()
    if form.validate_on_submit():
        event_date = form.event_date.data
        description = form.description.data
        # Ajouter l'événement dans la base de données
        flash('Event added successfully!', 'success')
        return redirect(url_for('.display'))
    # Récupérer les événements de la base de données pour les afficher
    events = [{'date': datetime.today(), 'description': 'Sample Event'}]  # Remplacer par des données réelles
    return render_template('event_calendar/calendar.html', form=form, events=events)
