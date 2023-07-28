from flask import Flask

def create_app_object():
    app = Flask("rh-ui app")

    return app

