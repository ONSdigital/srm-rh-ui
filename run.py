from rh_ui import app

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"], host="0.0.0.0", port=app.config["PORT"])
