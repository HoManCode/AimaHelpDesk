from app import db

# Models
class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    category=db.Column(db.String(100))
    department=db.Column(db.String(100))
    employee=db.Column(db.String(100))
    tel=db.Column(db.Integer)
    description = db.Column(db.String(512))

    def __repr__(self):
        return '<Task %r - %r - %r - %r - %r - %r>' % self.name, self.category, self.department, self.employee, self.tel, self.description