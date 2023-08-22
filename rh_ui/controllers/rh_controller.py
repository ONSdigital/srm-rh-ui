import hashlib
import re

import requests
from flask import current_app, flash, redirect, url_for, g
from requests import HTTPError

UAC_LENGTH = 16


def get_eq_token(uac: str, region: str):
    uac_hash = get_uac_hash(uac)
    response = get_eq_token_from_rh_svc(uac_hash, region)
    return response


def get_eq_token_from_rh_svc(uac_hash: str, region_code: str):
    rh_svc_url_token = (f'{current_app.config.get("RH_SVC_URL")}eqLaunch/{uac_hash}?languageCode={region_code}' +
                        f'&accountServiceUrl={current_app.config.get("ACCOUNT_SERVICE_URL")}')
    response = requests.get(rh_svc_url_token)
    try:
        response.raise_for_status()
    except HTTPError as ex:

        # TODO: look into implementing that as a flashed message rather than a separate page
        if ex.response.status_code == 400:
            return ex.response

        elif ex.response.status_code == 404:
            flash('uac_invalid')
            return redirect(url_for('i18n.start_bp.start_get', lang_code=g.lang_code))

    return response


def get_uac_hash(uac) -> str:
    uac_validation_pattern = re.compile(fr'^[A-Z0-9]{{{UAC_LENGTH}}}$')  # Outer 2 curly braces escape the f-string

    if not uac_validation_pattern.fullmatch(uac):  # yapf: disable
        raise TypeError

    return get_sha256_hash(uac)


def get_sha256_hash(uac: str) -> str:
    return hashlib.sha256(uac.encode()).hexdigest()
