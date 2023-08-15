from flask import flash 

def validate_uac(uac):
    if not uac:
        flash('uac_empty')
    if len(uac) != 16:
        flash('uac_invalid_length')
    # TODO handle invalid uac (no match in rh-service)