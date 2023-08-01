import os
import logging

from flask import Flask
from structlog import wrap_logger
from rh_ui.logger_config import logger_initial_config


def create_app():
    app = Flask("RH-UI app")

    app_config = "config.{}".format(os.environ.get("APP_CONFIG", "DevelopmentConfig"))
    app.config.from_object(app_config)

    # Configure logger
    logger_initial_config(log_level=app.config["LOGGING_LEVEL"])
    logger = wrap_logger(logging.getLogger(__name__))
    logger.debug("App configuration set", config=app_config)

    # Register blueprints
    from rh_ui.views.hello import hello_bp
    app.register_blueprint(hello_bp)

    return app
