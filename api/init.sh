#!/bin/sh

# First we need to setup the database
echo "Setting up database..."
python db.py

# Then just run the server
echo "Starting server..."
gunicorn app:'create_app()' -b:5000