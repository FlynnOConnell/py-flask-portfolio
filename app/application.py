from flask import Flask


# factory
def create_app(filename: str):
    app = Flask(__name__)
    app.config.from_object(filename)
    return app
