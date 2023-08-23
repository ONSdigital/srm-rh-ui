import hashlib
import re

import requests
from flask import current_app
from requests import Response

UAC_LENGTH = 16


def get_eq_token(uac: str, region: str) -> Response:
    uac_hash = get_uac_hash(uac)
    response = request_eq_launch_token(uac_hash, region)
    return response


def request_eq_launch_token(uac_hash: str, region_code: str) -> Response:
    rh_svc_url_token = (f'{current_app.config.get("RH_SVC_URL")}eqLaunch/{uac_hash}?languageCode={region_code}' +
                        f'&accountServiceUrl={current_app.config.get("ACCOUNT_SERVICE_URL")}')
    response = requests.get(rh_svc_url_token)
    return response


def get_uac_hash(uac: str) -> str:
    uac_validation_pattern = re.compile(fr'^[A-Z0-9]{{{UAC_LENGTH}}}$')  # Outer 2 curly braces escape the f-string

    if not uac_validation_pattern.fullmatch(uac):
        raise TypeError('Invalid UAC format for hashing')

    return get_sha256_hash(uac)


def get_sha256_hash(uac: str) -> str:
    return hashlib.sha256(uac.encode()).hexdigest()
