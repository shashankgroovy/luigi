import os
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


_DATABASE = os.environ.get('DATABASE_URL')
_default_schema_file = 'schema.sql'
_encoding = 'utf-8'


def get_db():
    """Get the database connection"""
    if 'db' not in g:
        g.db = sqlite3.connect(
            _DATABASE,
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    """Close connection to database"""
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    """Initialize the database"""
    db = get_db()

    with current_app.open_resource(_default_schema_file) as f:
        db.executescript(f.read().decode(_encoding))


# Register commands
@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    """Initialize the app"""
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
