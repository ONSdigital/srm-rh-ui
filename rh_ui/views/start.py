import logging
from flask import Blueprint, render_template, request, flash, g
from structlog import wrap_logger
from rh_ui.controllers import uac_validation
from rh_ui.views.lang_code_processing import setup_lang_code_processing
from flask_babel import refresh, _


logger = wrap_logger(logging.getLogger(__name__))

start_bp = Blueprint("start_bp", __name__, template_folder="templates", url_prefix='/<lang_code>')
setup_lang_code_processing(start_bp)

@start_bp.route("/start/", methods=["GET", "POST"])
def start_get():
    flash("Language code: " + g.lang_code)
    flash("Request metod: " + request.method)

    logger.info(f"received {request.method} on endpoint '{request.endpoint}'", 
                method=request.method,
                path=request.path)
    
    return render_template("start.html", page_title=_("title welsh"), lang_code=g.lang_code, domain_url="localhost:9092")

# cleaner way compared to putting it in the same function
@start_bp.route("/asda/", methods=["POST"])
def start_post():
    flash("POST received, lang code: " + g.lang_code)
    uac = request.form['uac']
    print(uac)

    try:
        validate_uac(uac)
    except:
        print("Validation failed")
