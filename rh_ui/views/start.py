import logging

from flask import Blueprint, render_template, request, flash, g, url_for, redirect, current_app
from flask.typing import ResponseReturnValue
from structlog import wrap_logger

from rh_ui.controllers import uac_validation
from rh_ui.controllers.lang_code_processing import setup_lang_code_processing
from rh_ui.controllers.rh_controller import get_eq_token

logger = wrap_logger(logging.getLogger(__name__))

start_bp = Blueprint("start_bp", __name__, template_folder="../templates", url_prefix='/<lang_code>')
setup_lang_code_processing(start_bp)

UAC_ERROR_PAGES = {
    'UAC_RECEIPTED': 'uac_error_pages/uac-already-used.html',
    'UAC_INACTIVE': 'uac_error_pages/uac-inactive.html'
}


@start_bp.route("/start/", methods=["GET"])
def start_get() -> ResponseReturnValue:
    logger.info(f"received {request.method} on endpoint '{request.endpoint}'",
                method=request.method,
                path=request.path)

    return render_template("start.html", lang_code=g.lang_code)


@start_bp.route("/start/", methods=["POST"])
def start_post():
    region = g.lang_code
    uac = request.form.get('access-code').upper().replace(' ', '')  # type: ignore
    error = uac_validation.validate_uac(uac)
    if error:
        flash(error)
        return redirect(url_for('start_bp.start_get', lang_code=g.lang_code))
    response = get_eq_token(uac, region)
    if response.status_code == 302:
        return response
    elif response.status_code == 400:
        return render_template(UAC_ERROR_PAGES[response.text], lang_code=g.lang_code)

    return redirect(f'{current_app.config["EQ_URL"]}/session?token={response.text}')
