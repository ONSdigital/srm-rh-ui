import logging
from flask import Blueprint, render_template, request, g, flash
from structlog import wrap_logger
from rh_ui.views.lang_code_processing import setup_lang_code_processing
from flask_babel import refresh


logger = wrap_logger(logging.getLogger(__name__))

info_pages_bp = Blueprint("info_pages_bp", __name__, template_folder="../templates", url_prefix='/<lang_code>')
setup_lang_code_processing(info_pages_bp)


@info_pages_bp.route("/cookies", methods=["GET"])
def cookies():
    logger.info(f"received {request.method} on endpoint '{request.endpoint}'",
                method=request.method,
                path=request.path)
    return render_template("cookies.html", lang_code=g.lang_code)

@info_pages_bp.route("/privacy-and-data-protection", methods=["GET"])
def privacy_and_data_protection():
    logger.info(f"received {request.method} on endpoint '{request.endpoint}'",
                method=request.method,
                path=request.path)
    return render_template("privacy-and-data-protection.html", lang_code=g.lang_code)
