from application import app, db
from application.models import ToDos
from flask import redirect, url_for, render_template

@app.route('/')
def index():
    todo = ToDos.query.all()
    empstr = ""
    for t int todo:
        empstr += f'{t.id} {t.task} {t.completed} \n'

    return empstr

@app.route('/about')
def index():
    return render_template('about.html')

@app.route('/tasks')
def index():
    return render_template('tasks.html')

@app.route('/add/<new_task>')
def add(new_task):
    task_to_add = ToDos(task=new_task)
    db.session.add(task_to_add)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/complete/<int:id>')
def complete(id):
    todo = ToDos.query.get(id)
    todo.completed = True
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/incomplete/<int:id>')
def incomplete(id):
    todo = ToDos.query.get(id)
    todo.completed = False
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>/<new_task>')
def update(id, new_task):
    todo = ToDos.query.get(id)
    todo.task = new_task
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<del_task>')
def delete(del_task):
    todo = ToDos.query.filter_by(task=del_task).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))
