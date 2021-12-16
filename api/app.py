"""
The entry point for the API server.

There are 3 primary things that are happening in this file:
    - The server is being created and configured.
    - All flask blueprints are being imported and registered.
    - Redis and SQLite are being configured.
"""
import os

from flask import Flask, jsonify
from flask_cors import CORS

from v1.api import api_v1

app = Flask("api")

# Enable CORS
CORS(app)

# Initialize the database
try:
    import db
    db.init_app(app)
except ImportError:
    pass

# Register blueprints
app.register_blueprint(api_v1, url_prefix="/v1")

# Add the health check route.
@app.route('/health')
def health():
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    app.run(host=os.environ.get('APP_HOST'),
            port=os.environ.get('APP_PORT', 5000))
