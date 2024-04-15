from flask import render_template, redirect, url_for, flash, session
from .forms import LeaveRequestForm
from .models import LeaveRequest, db

def new_leave():
    if not session.get('logged_in'):
        return redirect(url_for('auth.login'))
    form = LeaveRequestForm()
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
        return redirect(url_for('.view_calendar'))
    return render_template('event_calendar/submit_leave.html', form=form)

def view_calendar():
    leave_requests = LeaveRequest.query.all()
    return render_template('event_calendar/view_calendar.html', leave_requests=leave_requests)
