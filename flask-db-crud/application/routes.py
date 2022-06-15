@app.route('/')
def index():
    todo = ToDos.query.first()
    return f'Task: {todo.task} Completed: {todo.completed} '

@app.route('/add/<new_task>')
def add(new_task):
    task_to_add = ToDos(task=new_task)
    db.session.add(task_to_add)
    db.session.commit()
    return 'Added a new todo'

@app.route