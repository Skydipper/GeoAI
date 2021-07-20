#!/bin/bash
set -e

case "$1" in
    develop)
        echo "Running Development Server"
        exec python main.py
        ;;
    test)
        echo "Running tests"
        exec pytest --cov=geoai geoai/tests/
        ;;
    start)
        echo "Running Start"
        exec gunicorn -c gunicorn.py geoai:app
        ;;
    *)
        exec "$@"
esac
