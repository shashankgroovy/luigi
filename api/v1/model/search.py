import sqlite3
from flask import g

import logger

logger = logger.get_logger()

def save_search(search_term, external_ip):
    """
    Saves the search term to the database.
    """
    # Obtain a connection to the database

    try:
        query = "INSERT INTO searches (externalUserIp, query) VALUES (?, ?)"
        g.db.execute(query, (external_ip, search_term))
        g.db.commit()

    except sqlite3.OperationalError as e:
        logger.error(f'Error while saving search term to database: {e}',
                     f'Please re-initialize the database')