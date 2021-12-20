import os
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


_default_schema_file = 'schema.sql'
_encoding = 'utf-8'


def get_db():
    """Get the database connection"""
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE_URL'],
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
    db = sqlite3.connect(
        os.environ.get('DATABASE_URL'),
        detect_types=sqlite3.PARSE_DECLTYPES
    )

    with open(_default_schema_file, encoding=_encoding) as f:
        db.executescript(f.read())


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


if __name__ == '__main__':
    init_db()
    print('Initialized the database.')