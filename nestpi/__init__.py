import os
from flask import Flask, redirect, url_for

from nestpi import db
from nestpi import auth


def create_app(test_config=None):
    """
    Flask application factory function.
    """

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "nestpi.sqlite"),
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello/")
    def hello():
        return "Hello, World!"

    @app.route("/index/")
    def index():
        return redirect(url_for("hello"))

    db.init_app(app)

    app.register_blueprint(auth.bp)

    return app
