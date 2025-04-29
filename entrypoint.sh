#!/bin/sh

poetry run alembic upgrade head

echo "Starting up..."
exec poetry run litestar --app src.app:app run --host "0.0.0.0" --port 8000