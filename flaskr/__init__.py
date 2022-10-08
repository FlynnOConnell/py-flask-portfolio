"""
web_dataviewer/__init__.py

Entry point for dataviewer app. Flask docs recommend larger app initializing to be done here.
"""


import os
from pathlib import Path
from flask import (Flask, current_app)
from werkzeug.local import LocalProxy

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\flynn\repos\web_dataviewer\JSON_credentials.json"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
dirname = os.path.dirname(os.path.abspath(__file__))
logger = LocalProxy(lambda: current_app.logger)



def create_app(test_config=None):
    # config files relative to the instance folder
    # outside dataviewer package, hold local data not
    # commited to vc
    app = Flask(__name__, instance_relative_config=True)

    # app.config.from_object('yourapplication.default_settings')
    # app.config.from_envvar('YOURAPPLICATION_SETTINGS')
    import os

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('default_settings.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from flaskr import home
    app.register_blueprint(home.bp)
    return app

if __name__ == "__main__":
    from waitress import serve
    app = create_app()
    app.config["DEBUG"]=True
    serve(app, host='0.0.0.0', port=8080)
