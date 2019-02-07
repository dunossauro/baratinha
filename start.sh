export FLASK_ENV=development
export FLASK_APP=app
flask db upgrade
# flask run --host=0.0.0.0
gunicorn "app:create_app()" --bind localhost:5000 --workers=3 --log-level INFO
