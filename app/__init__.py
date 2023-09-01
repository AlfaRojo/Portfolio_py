from . import portfolio
from flask import Flask
import os


def crete_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SENDGRID_KEY = os.environ.get('SENDGRID_KEY'),
    )

    app.register_blueprint(portfolio.bp)
    return app

app = crete_app()