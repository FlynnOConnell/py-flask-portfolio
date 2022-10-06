import os
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

    # set some default configs
    app.config.from_mapping(
            SECRET_KEY='dev',
            UPLOAD_FOLDER=dirname + '/flaskr/static/uploads',
            DATABASE=os.path.join(app.instance_path, 'web_dataviewer.sqlite'),
            MAX_CONTENT_LENGTH=16 * 1024 * 1024
        )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from app import home, view
    app.register_blueprint(home.bp)
    return app
