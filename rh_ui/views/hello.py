import logging
from flask import Blueprint, render_template
from structlog import wrap_logger

# logger = wrap_logger(logging.getLogger(__name__))

hello_bp = Blueprint("hello_bp", __name__, template_folder="../templates")

@hello_bp.route("/", methods=["GET"])
def hello():
    return render_template("hello.html")
