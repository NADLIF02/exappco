from flask import render_template, redirect, url_for, flash, session
from .forms import EventForm  # Ensure this import is correct
from .models import LeaveRequest, db  # Assuming you have models set up

@app.route('/leave/new', methods=['GET', 'POST'])
def new_leave():
    form = EventForm()
    if form.validate_on_submit():
        leave_request = LeaveRequest(
            employee_name=form.employee_name.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            reason=form.reason.data
        )
        db.session.add(leave_request)
        db.session.commit()
        flash('Leave request submitted successfully!')
        return redirect(url_for('event_calendar.view_calendar'))
    return render_template('event_calendar/submit_leave.html', form=form)

@app.route('/leave/view')
def view_calendar():
    leave_requests = LeaveRequest.query.all()
    return render_template('event_calendar/view_calendar.html', leave_requests=leave_requests)
