from flask import Flask

from config import Config
from database import db


def create_app():
    application = Flask(__name__)
    application.config.from_object(Config)
    application.app_context().push()
    db.init_app(application)

    return application



app = create_app()
with app.app_context():
    db.create_all()
