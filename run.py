import os
from rh_ui import app

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"], host="127.0.0.1", port=app.config["PORT"])
