from rh_ui.app_setup import create_app
# from rh_ui.security import build_response_headers

app = create_app()


if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"], host="0.0.0.0", port=app.config["PORT"])
