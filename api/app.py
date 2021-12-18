"""
The entry point for the API server.

There are 3 primary things that are happening in this file:
    - The server is being created and configured.
    - All flask blueprints are being imported and registered.
    - Redis and SQLite are being configured.
"""
import os

from flask import Flask, g, jsonify
from flask_caching import Cache
from flask_cors import CORS

from logger import get_logger

# Set the cache instance and log as a global variable.
cache = Cache()
log = get_logger()


def create_app():
    """
    Create and configure the API server.
    """
    log.info('Initializing API server')
    app = Flask("api", instance_relative_config=True)
    app.config.from_object('config.BaseConfig')

    # Enable CORS
    log.info("Enabling CORS")
    CORS(app)

    # Initialize the caching layer
    log.info("Initializing the cache layer")
    cache.init_app(app, config={'CACHE_TYPE': app.config['CACHE_TYPE']})

    # Initialize the database
    import db
    log.info("Initializing the database")
    db.init_app(app)

    # Add a health check route.
    @app.route('/health')
    def health():
        return jsonify({'status': 'ok'})

    # Register all blueprints
    from v1.api import api_v1
    app.register_blueprint(api_v1, url_prefix="/v1")
    log.info("Registering API v1 routes")

    # Return the app
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host=os.environ.get('APP_HOST'),
            port=os.environ.get('APP_PORT', 5000))
