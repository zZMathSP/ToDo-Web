import os

from werkzeug.utils import secure_filename
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object('project.config.Config')
db = SQLAlchemy(app)
from project import routes, models

migrate = Migrate(app, db)

