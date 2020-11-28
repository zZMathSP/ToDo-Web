from flask.cli import FlaskGroup

from project import app, db
from project.models import Todo


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(Todo(description="Todo 1"))
    db.session.add(Todo(description="Todo 2"))
    db.session.add(Todo(description="Todo 3"))
    db.session.commit()


@cli.command("migrate")
def migrate():
    migrate = Migrate(app, db)
    manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    cli()
