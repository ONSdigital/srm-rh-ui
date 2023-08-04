from rh_ui.app_setup import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=app.config["DEBUG"], host="0.0.0.0", port=app.config["PORT"])
