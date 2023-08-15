import logging
from flask import Blueprint, render_template, request, flash, g, url_for, redirect, abort
from structlog import wrap_logger
from rh_ui.controllers import uac_validation
from rh_ui.views.lang_code_processing import setup_lang_code_processing
from flask_babel import refresh, _

logger = wrap_logger(logging.getLogger(__name__))

start_bp = Blueprint("start_bp", __name__, template_folder="templates", url_prefix='/<lang_code>')
setup_lang_code_processing(start_bp)


@start_bp.route("/start/", methods=["GET"])
def start_get():
    flash("Language code: " + g.lang_code)
    flash("Request metod: " + request.method)

    logger.info(f"received {request.method} on endpoint '{request.endpoint}'",
                method=request.method,
                path=request.path)
    error = request.data
    # if error:
    #    return render_template("start.html", lang_code=g.lang_code, field_messages_dict=error)
    return render_template("start.html", lang_code=g.lang_code)


# cleaner way compared to putting it in the same function
@start_bp.route("/start/", methods=["POST"])
def start_post():
    flash("POST received, lang code: " + g.lang_code)
    uac = request.form.get('access-code').upper().replace(' ', '')
    if not uac:
        return redirect(url_for('start_bp.start_get', data='uac_empty'))
    if len(uac) != 16:
        return redirect(url_for('start_bp.start_get', data='uac_invalid_length'))

    return redirect(url_for('start_bp.start_get', lang_code=g.lang_code, values=None))
