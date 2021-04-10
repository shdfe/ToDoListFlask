from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(50), index=True)
    status = db.Column(db.Boolean, default=False, index=True)

    def __repr__(self):
        return f'<Task {self.task}>'
