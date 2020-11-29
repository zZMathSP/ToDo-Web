import click
from flask.cli import FlaskGroup

from project import app, db
from project.models import Todo


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.create_all()
    db.session.commit()


@cli.command("reset_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("drop_db")
def drop_db():
    db.drop_all()
    db.session.commit()


if __name__ == "__main__":
    cli()
