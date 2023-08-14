import os
import logging

from flask import Flask, g
from flask_babel import Babel
from structlog import wrap_logger
from rh_ui.logger_config import logger_initial_config
from requests import request
from werkzeug.exceptions import HTTPException


def create_app():
    app = Flask("RH-UI app")
     
    def get_locale():
        if not g.get('lang_code', None):
            g.lang_code = request.accept_languages.best_match(app.config["LANGUAGES"])
        return g.lang_code

    app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'rh_ui/translations'

    babel = Babel(app, locale_selector=get_locale)

    app_config = f'config.{os.environ.get("APP_CONFIG", "DevelopmentConfig")}'
    app.config.from_object(app_config)

    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' # required to enable the flash function

    # Configure logger
    logger_initial_config(log_level=app.config["LOGGING_LEVEL"])
    logger = wrap_logger(logging.getLogger(__name__))
    logger.debug("App configuration set", config=app_config)

    # Register blueprints
    from rh_ui.views.hello import hello_bp
    app.register_blueprint(hello_bp)
    from rh_ui.views.start import start_bp
    app.register_blueprint(start_bp)
    from rh_ui.views.info_pages import info_pages_bp
    app.register_blueprint(info_pages_bp)

    # Register error handlers
    from rh_ui.views.error_handlers import handle_404
    app.register_error_handler(404, handle_404)
    from rh_ui.views.error_handlers import handle_404
    app.register_error_handler(404, handle_404)
    # from rh_ui.views.error_handlers import handle_error
    # app.register_error_handler(HTTPException.code, handle_error)

    return app
