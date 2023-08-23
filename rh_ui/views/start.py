import logging

from flask import Blueprint, request, flash, g, redirect, current_app
from flask.typing import ResponseReturnValue
from requests import Response, HTTPError
from structlog import wrap_logger

from rh_ui.controllers.rh_service import get_eq_token
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
    uac = request.form.get('access-code').upper().replace(' ', '')
    if error := pre_check_uac(uac):
        flash(error)
        return redirect(url_for_i18n('start_bp.start_get'))
    token_response = get_eq_token(uac, g.lang_code)

    if error_response := handle_token_error_response(token_response):
        return error_response

    return redirect(f'{current_app.config["EQ_URL"]}/session?token={token_response.text}')


def pre_check_uac(uac: str) -> str | None:
    if not uac:
        error = 'uac_empty'
        return error
    if len(uac) != 16:
        error = 'uac_invalid_length'
        return error
    return None


def handle_token_error_response(response: Response):
    try:
        response.raise_for_status()
    except HTTPError as ex:

        # TODO: look into implementing that as a flashed message rather than a separate page
        if ex.response.status_code == 400:
            return render_template_i18n(UAC_ERROR_PAGES[response.text])
        elif response.status_code == 302:
            return response
        elif ex.response.status_code == 404:
            flash('uac_invalid')
            return redirect(url_for_i18n('start_bp.start_get'))
        raise ex
