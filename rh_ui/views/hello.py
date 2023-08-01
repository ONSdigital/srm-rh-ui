import logging
from flask import Blueprint, render_template, request
from structlog import wrap_logger

logger = wrap_logger(logging.getLogger(__name__))

hello_bp = Blueprint("hello_bp", __name__, template_folder="../templates")


@hello_bp.route("/hello", methods=["GET"])
def hello():
    logger.info(f"received {request.method} on endpoint '{request.endpoint}'",
                method=request.method,
                path=request.path)
    return render_template("hello.html")
