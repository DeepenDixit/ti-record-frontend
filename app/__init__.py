from flask import Flask

from app.blueprints.auth import auth_bp
from app.blueprints.record_filter import record_filter_bp
from app.core.config import settings


def create_app():
    """Main flask app"""
    app = Flask(__name__)
    app.config["SECRET_KEY"] = settings.FLASK_SECRET_KEY
    app.config["WTF_CSRF_ENABLED"] = False

    app.register_blueprint(auth_bp, url_prefix="/")
    app.register_blueprint(record_filter_bp, url_prefix="/")

    return app
