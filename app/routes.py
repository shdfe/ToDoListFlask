from flask import render_template, redirect, url_for
from app import app, db
from app.forms import TaskForm
from app.models import Task




@app.route('/', methods=['GET', 'POST'])
def index():
    form = TaskForm()

    if form.validate_on_submit():
        db.session.add(Task(task=form.task.data, status=False))
        db.session.commit()
        return redirect(url_for('index'))
    tasks = Task.query.all()
    return render_template('index.html', form=form, tasks=tasks)

@app.route('/complete/<id>')
def complete(id):
    todo = Task.query.filter_by(id=int(id)).first()
    todo.status = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/incomplete/<id>')
def incomplete(id):
    todo = Task.query.filter_by(id=int(id)).first()
    todo.status = False
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<id>')
def delete(id):
    todo = Task.query.filter_by(id=int(id)).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))