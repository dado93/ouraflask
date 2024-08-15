from flask import Flask
import os
import dotenv

dotenv.load_dotenv(dotenv_path="../.env")

from . import oura


def create_app(test_config=None):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    # create and configure app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev", DATABASE=os.path.join(app.instance_path, "flaskr.sqlite")
    )

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(oura.bp)
    app.add_url_rule("/", endpoint="login")
    # app.add_url_rule("/callback", endpoint="callback")
    # app.add_url_rule("/profile", endpoint="profile")

    return app
