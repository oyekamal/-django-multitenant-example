#!/bin/bash

# Wait for the database to be ready
echo "Waiting for PostgreSQL to be ready..."
until pg_isready -h db -U multitenant_user; do
  echo "PostgreSQL is unavailable - sleeping"
  sleep 1
done
echo "PostgreSQL is up!"


python manage.py makemigrations
python manage.py migrate
# # Run shared migrations
# echo "Running shared migrations..."
# python manage.py migrate_schemas --shared

# # Run tenant migrations
# echo "Running tenant migrations..."
# python manage.py migrate_schemas

# Start the Django development server
echo "Starting Django server..."
exec python manage.py runserver 0.0.0.0:8000
