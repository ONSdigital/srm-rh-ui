from rh_ui.app_setup import create_app
from flask_talisman import Talisman
from rh_ui.security import build_response_headers, CSP

app = create_app()
talisman = Talisman(
        app,
        content_security_policy=CSP,
        content_security_policy_nonce_in=['script-src'],
        force_https=False,
        frame_options='DENY',
        strict_transport_security='max-age=31536000; includeSubDomains'

    )


@app.after_request
def add_security_headers(resp):
    resp.headers = build_response_headers()
    return resp


if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"], host="0.0.0.0", port=app.config["PORT"])
