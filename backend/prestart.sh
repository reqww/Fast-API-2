#! /bin/bash

sleep 10;

poetry run alembic upgrade head

exec "$@"