from flask import g

def save_search(search_term, external_ip):
    """
    Saves the search term to the database.
    """
    # Obtain a connection to the database

    try:
        query = "INSERT INTO searches (externalUserIp, query) VALUES (?, ?)"
        g.db.execute(query, (external_ip, search_term))
        g.db.commit()

    except g.db.IntegrityError:
        # Well this is awkward.
        pass
