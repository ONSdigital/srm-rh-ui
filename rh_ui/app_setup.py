import logging
import os

from flask import Flask, g, request
from flask_babel import Babel
from structlog import wrap_logger

from rh_ui.logger_config import logger_initial_config


def create_app() -> Flask:
    app = Flask("RH-UI app")

    # Babel setup
    def get_locale() -> str:
        if not g.get('lang_code', None):
            g.lang_code = request.accept_languages.best_match(app.config["LANGUAGES"])
        return g.lang_code

    app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'rh_ui/translations'
    Babel(app, locale_selector=get_locale)

    # App config setup
    app_config = f'config.{os.environ.get("APP_CONFIG", "BaseConfig")}'
    app.config.from_object(app_config)
    app.secret_key = app.config.get('SECRET_KEY')  # required to enable the flash function

    # Configure logger
    logger_initial_config(log_level=app.config.get("LOGGING_LEVEL", "INFO"))
    logger = wrap_logger(logging.getLogger(__name__))
    logger.debug("App configuration set", config=app_config)

    # Register the i18n blueprint, which all internationalised routes are registered below
    from rh_ui.views.i18n import i18n
    app.register_blueprint(i18n)
    from rh_ui.views.healthcheck import healthcheck_bp
    app.register_blueprint(healthcheck_bp)
    # Register error handlers
    from rh_ui.views.error_handlers import handle_404
    app.register_error_handler(404, handle_404)
    from rh_ui.views.error_handlers import handle_500
    app.register_error_handler(500, handle_500)

    return app
