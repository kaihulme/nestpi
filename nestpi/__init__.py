import os
from flask import Flask, redirect, url_for, render_template

from nestpi import db, auth


def create_app(test_config=None):
    """
    Flask application factory function.
    """
    application = Flask(__name__, instance_relative_config=True)
    application.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(application.instance_path, "nestpi.sqlite"),
    )

    if test_config is None:
        application.config.from_pyfile("config.py", silent=True)
    else:
        application.config.from_mapping(test_config)

    try:
        os.makedirs(application.instance_path)
    except OSError:
        pass

    @application.route("/home/")
    def hello():
        return render_template("home.html")

    @application.route("/")
    def index():
        return redirect(url_for("hello"))

    db.init_app(application)

    application.register_blueprint(auth.bp)

    return application
