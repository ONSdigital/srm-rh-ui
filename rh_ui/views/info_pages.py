import logging

from flask import Blueprint, request
from structlog import wrap_logger

from rh_ui.i18n_helpers import render_template_i18n

logger = wrap_logger(logging.getLogger(__name__))

info_pages_bp = Blueprint("info_pages_bp", __name__, template_folder="../templates/info_pages")


@info_pages_bp.route("/cookies", methods=["GET"])
def cookies() -> str:
    logger.info(f"received {request.method} on endpoint '{request.endpoint}'",
                method=request.method,
                path=request.path)
    return render_template_i18n("cookies.html")


@info_pages_bp.route("/privacy-and-data-protection", methods=["GET"])
def privacy_and_data_protection() -> str:
    logger.info(f"received {request.method} on endpoint '{request.endpoint}'",
                method=request.method,
                path=request.path)
    return render_template_i18n("privacy-and-data-protection.html")
