import os

from werkzeug.utils import secure_filename
from flask import (
    Flask,
    request,
    redirect,
    url_for,
    render_template,
    jsonify
)
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('project.config.Config')
db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}'
        

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

@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())

