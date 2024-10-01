from flask import Blueprint, redirect, render_template, request, session, url_for

from app.core.config import settings
from app.core.constants import LoginPage, SessionKeys, TemplateNames
from app.utils.logger_helper import app_logger

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("")
def index():
    """
    Function to display the login page
    """
    if session.get(SessionKeys.LOGGED_IN):
        app_logger.info(
            "User landed on landing page: %s", session.get(SessionKeys.USERNAME)
        )
        return render_template(TemplateNames.INDEX)
    return render_template(TemplateNames.LOGIN)


@auth_bp.route("login", methods=["GET", "POST"])
def login():
    """
    Function to login user
    """
    if request.method == "POST":
        username = request.form.get(LoginPage.USERNAME)
        password = request.form.get("password")

        if (
            username == settings.DEFAULT_APP_USER
            and password == settings.DEFAULT_APP_PASSWORD
        ):
            session[SessionKeys.LOGGED_IN] = True
            session[SessionKeys.USERNAME] = username
            app_logger.info("Access authorized for user: %s", username)

            return redirect(url_for("auth.index"))

        app_logger.info("Unauthorized attempt made by user: %s", username)
        return render_template(TemplateNames.LOGIN)

    if session.get(SessionKeys.LOGGED_IN):
        return redirect(url_for("auth.index"))

    return render_template(TemplateNames.LOGIN)


@auth_bp.route("logout")
def logout():
    """
    Function to logout user
    """
    if SessionKeys.LOGGED_IN in session:
        session.pop(SessionKeys.LOGGED_IN)
        session.pop(SessionKeys.USERNAME)
    return render_template(TemplateNames.LOGIN)
