from app import db

class LeaveRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    reason = db.Column(db.String(200))

    def __repr__(self):
        return f'<LeaveRequest {self.employee_name} from {self.start_date} to {self.end_date}>'
