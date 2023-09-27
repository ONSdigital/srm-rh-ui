CSP = {
    'default-src': [
        "'self'",
        'https://cdn.ons.gov.uk',
    ],
    'font-src': [
        "'self'",
        'data:',
        'https://cdn.ons.gov.uk',
    ],
    'script-src': [
        "'self'",
        'https://*.googletagmanager.com',
        'https://cdn.ons.gov.uk',
    ],
    'connect-src': [
        "'self'",
        'https://cdn.ons.gov.uk',
        'https://*.google-analytics.com',
        'https://*.analytics.google.com',
        'https://*.googletagmanager.com'
    ],
    'img-src': [
        "'self'",
        'data:',
        'https://*.google-analytics.com',
        'https://*.googletagmanager.com',
        'https://cdn.ons.gov.uk'
    ],
    'style-src': [
        "'self'", 
        'https://cdn.ons.gov.uk',
        "'unsafe-inline'",
        'https://tagmanager.google.com',
        'https://fonts.googleapis.com'
    ,]

}

DEFAULT_RESPONSE_HEADERS = {
    'X-Frame-Options': 'DENY',
    'X-Content-Type-Options': 'nosniff',
    'Referrer-Policy': 'strict-origin-when-cross-origin',
    'X-Permitted-Cross-Domain-Policies': 'None',
    'clear-site-data': '"storage"',
    'Cross-Origin-Opener-Policy': 'same-origin',
    'Cross-Origin-Resource-Policy': 'same-site',
    'Cache-Control': ['no-store', 'max-age=0'],
    'Server': 'Office For National Statistics',
    'Permissions-Policy': 'accelerometer=(),autoplay=(),camera=(),display-capture=(),document-domain=(),'
                          'encrypted-media=(),fullscreen=(),geolocation=(),gyroscope=(),magnetometer=(),microphone=('
                          '),midi=(),payment=(),picture-in-picture=(),publickey-credentials-get=(),screen-wake-lock=('
                          '),sync-xhr=(self),usb=(),xr-spatial-tracking=()'
}


def build_response_headers():
    headers = {}
    for header, value in DEFAULT_RESPONSE_HEADERS.items():
        if isinstance(value, dict):
            value = '; '.join([
                f"{section} {' '.join(content)}"
                for section, content in value.items()
            ])
        elif not isinstance(value, str):
            value = ' '.join(value)
        headers[header] = value
    return headers
