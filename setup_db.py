from app import app, db
from app.models import Task

db.drop_all()
db.create_all()

tasks = [
    'Software Issue',
    'Hardware Issue',
    'Network Issue',
    'Internet Issue',
    'Other Issue, Please describe the issue in the text box'
]

for task in tasks:
    new_task = Task(name=task, description='')
    db.session.add(new_task)
db.session.commit()