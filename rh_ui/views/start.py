import logging

from flask import Blueprint, request, flash, g, redirect, current_app
from flask.typing import ResponseReturnValue
from structlog import wrap_logger

from rh_ui.controllers import uac_validation
from rh_ui.controllers.rh_controller import get_eq_token
from rh_ui.i18n_helpers import url_for_i18n, render_template_i18n

logger = wrap_logger(logging.getLogger(__name__))

start_bp = Blueprint("start_bp", __name__, template_folder="../templates")

UAC_ERROR_PAGES = {
    'UAC_RECEIPTED': 'uac_error_pages/uac-already-used.html',
    'UAC_INACTIVE': 'uac_error_pages/uac-inactive.html'
}


@start_bp.route("/start/", methods=["GET"])
def start_get() -> ResponseReturnValue:
    logger.info(f"received {request.method} on endpoint '{request.endpoint}'",
                method=request.method,
                path=request.path)

    return render_template_i18n("start.html")


@start_bp.route("/start/", methods=["POST"])
def start_post():

    uac = request.form.get('access-code').upper().replace(' ', '')  # type: ignore
    error = uac_validation.validate_uac(uac)
    if error:
        flash(error)
        return redirect(url_for_i18n('start_bp.start_get'))
    response = get_eq_token(uac, g.lang_code)
    if response.status_code == 302:
        return response
    elif response.status_code == 400:
        return render_template_i18n(UAC_ERROR_PAGES[response.text])

    return redirect(f'{current_app.config["EQ_URL"]}/session?token={response.text}')
