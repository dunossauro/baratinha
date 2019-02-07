from flask import Flask
from app import models, schemas


def create_app():
    app = Flask(__name__)

    models.configure(app)
    schemas.configure(app)

    return app
