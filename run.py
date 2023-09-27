from rh_ui.app_setup import create_app
from rh_ui.security import build_response_headers

app = create_app()


@app.after_request
def add_security_headers(resp):
    resp.headers.extend(build_response_headers())
    return resp


if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"], host="0.0.0.0", port=app.config["PORT"])
