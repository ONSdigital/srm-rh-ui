import hashlib
import re

import requests
from flask import current_app, flash, redirect, url_for, g
from requests import Response, HTTPError

UAC_LENGTH = 16


def get_eq_token(uac: str, region: str) -> Response:
    uac_hash = get_uac_hash(uac)
    response = get_eq_token_from_rh_svc(uac_hash, region)
    return response


def get_eq_token_from_rh_svc(uac_hash: str, region_code: str) -> Response:
    rh_svc_url_token = (f'{current_app.config.get("RH_SVC_URL")}eqLaunch/{uac_hash}?languageCode={region_code}' +
                        f'&accountServiceUrl={current_app.config.get("ACCOUNT_SERVICE_URL")}')
    response = requests.get(rh_svc_url_token)
    try:
        response.raise_for_status()
    except HTTPError:
        flash('uac_invalid')
        return redirect(url_for('start_bp.start_get', lang_code=g.lang_code))
    return response


def get_uac_hash(uac):
    uac_validation_pattern = re.compile(fr'^[A-Z0-9]{{{UAC_LENGTH}}}$')  # Outer 2 curly braces escape the f-string

    if not uac_validation_pattern.fullmatch(uac):  # yapf: disable
        raise TypeError

    return get_sha256_hash(uac)


def get_sha256_hash(uac: str):
    return hashlib.sha256(uac.encode()).hexdigest()
