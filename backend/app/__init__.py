from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from app.config import Config
from app.database.db import db

# Authentication Blueprint
from app.auth.auth_routes import auth_bp

# Project Blueprint
from app.routes.project_routes import project_bp

# Initialize extensions
bcrypt = Bcrypt()
jwt = JWTManager()


def create_app():

    # Create Flask application
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    CORS(app)

    # Create database tables
    with app.app_context():
        try:
            db.create_all()
            print("Database connected successfully.")
        except Exception as e:
            print(f"Database connection failed: {e}")

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(project_bp)

    # Home API
    @app.route("/")
    def home():
        return {
            "application": "SecureOps DevSecOps Platform",
            "version": "1.0.0",
            "status": "Running",
            "message": "Welcome to SecureOps API"
        }, 200

    # Health API
    @app.route("/health")
    def health():
        return {
            "status": "UP",
            "database": "Connected",
            "service": "SecureOps Backend"
        }, 200

    return app