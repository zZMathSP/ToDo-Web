from flask import (
    Flask,
    request,
    redirect,
    url_for,
    render_template,
    jsonify
)
from project import app, db
from project.models import Todo

@app.route('/todos/create', methods=['POST'])
def create_todo():
    error = False
    body = {}
    try:
        description = request.get_json()['description']
        todo = Todo(description=description)
        db.session.add(todo)
        db.session.commit()
        body['description'] = todo.description
    except:
        error = True
        db.session.rollback()
    finally:
        db.session.close()
        if not error:
            return jsonify(body)


@app.route('/todos/<todo_id>/set-completed', methods=['POST'])
def set_completed_todos(todo_id):
    try:
        completed = request.get_json()['completed']
        todo = Todo.query.get(todo_id)
        todo.completed = completed
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()

    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.order_by('id').all())