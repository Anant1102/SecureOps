from flask import Flask
from .config import Config
from .database.db import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    @app.get("/health")
    def health():
        return {
            "status": "UP",
            "application": "SecureOps",
            "version": "1.0.0"
        }, 200

    return app
