import functools

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash
from requests_oauthlib import OAuth2Session

# from ouraflask.db import get_db
import requests

import os

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=["GET"])
def oura_login():
    """Redirect to the OAuth provider login page."""

    oura_session = OAuth2Session(
        os.environ.get("CLIENT_ID", None),
        scope=["personal", "daily", "heartrate", "workout", "tag", "session", "spo2"],
    )

    # URL for Oura's authorization page.
    authorization_url, state = oura_session.authorization_url(
        os.environ.get("AUTH_URL", None)
    )
    session["oauth_state"] = state
    return redirect(authorization_url)


@bp.route("/profile")
def profile():
    """User profile."""
    oauth_token = session["oauth"]["access_token"]
    url = "https://api.ouraring.com/v2/usercollection/daily_sleep"
    params = {"start_date": "2024-01-01", "end_date": "2024-07-01"}
    headers = {"Authorization": f"Bearer {oauth_token}"}
    response = requests.request("GET", url, headers=headers, params=params)
    return response.text


@bp.route("/callback")
def callback():
    """Retrieve acces_token from Oura response url. Redirect to profile page."""
    oura_session = OAuth2Session(
        os.environ.get("CLIENT_ID", None), state=session["oauth_state"]
    )
    session["oauth"] = oura_session.fetch_token(
        os.environ.get("TOKEN_URL", None),
        client_secret=os.environ.get("CLIENT_SECRET", None),
        authorization_response=request.url,
    )

    return redirect(url_for(".profile"))
