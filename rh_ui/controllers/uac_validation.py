def validate_uac(uac):
    if not uac:
        error = 'uac_empty'
        return error
    if len(uac) != 16:
        error = 'uac_invalid_length'
        return error