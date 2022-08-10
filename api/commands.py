from flask.cli import with_appcontext
import click

from api.extensions import db

@click.command('create_tables')
@with_appcontext
def create_tables():
    db.create_all()