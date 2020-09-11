from flask import render_template, request, redirect, url_for
from app import app, models, db
from flask import render_template, request, redirect, url_for, jsonify

Task = models.Task

@app.route('/')
def index():
    title = 'Aima Help Desk'
    tasks = Task.query.all()
    return render_template("index.html", title=title, tasks=tasks)

    # POST (Forms)
@app.route('/task/', methods=['POST'])
def add_item():
    # Get data from form fields taskName and taskDescription
    taskName = request.form.get('taskName')
    taskCategory=request.form.get('taskCategory')
    taskDepartment=request.form.get('taskDepartment')
    taskEmployee=request.form.get('taskEmployee')
    taskTel=request.form.get('taskTel')
    taskDescription = request.form.get('taskDescription')
    
    # Put data into a new Task item
    new_item = Task(name=taskName, category=taskCategory, department=taskDepartment, employee=taskEmployee, tel=taskTel, description=taskDescription)

    # Add and commit the changes to the database
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('index'))

    # DELETE (Delete a specific task id)
@app.route('/task/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.filter_by(id=id).first()
    
    # Check if Task exists
    if (task != None):
        msg = {
            'message': 'Delete successful'
        }
        db.session.delete(task)
        db.session.commit()
        return jsonify(msg), 200
	
    # Task does not exist
    msg = {
        'message': 'Task not found'
    }
    return jsonify(msg), 204

    # GET / UPDATE ID
@app.route('/task/<int:id>', methods=['GET', 'POST'])
def view_task(id):
    if (request.method == "GET"):
        task = Task.query.filter_by(id=id).first()
        return render_template('view_task.html', taskName=task.name, taskCategory=task.category, taskDepartment=task.department, taskEmployee=task.employee, taskTel=task.tel , taskDescription=task.description, taskId=task.id)
    elif (request.method == "POST"):
        taskId = request.form.get('taskId')
        taskName = request.form.get('taskName')
        taskCategory=request.form.get('taskCategory')
        taskDepartment=request.form.get('taskDepartment')
        taskEmployee=request.form.get('taskEmployee')
        taskTel=request.form.get('taskTel')
        taskDescription = request.form.get('taskDescription')

        task = Task.query.filter_by(id=id).first()
        if (task != None):
            task.name = taskName
            task.category=taskCategory
            task.department=taskDepartment
            task.employee=taskEmployee
            task.tel=taskTel
            task.description = taskDescription
            db.session.add(task)
            db.session.commit()
        return redirect(url_for('index'))