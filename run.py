import os
from rh_ui import app # NOQA

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"], host="127.0.0.1", port=app.config.get("PORT", 8082))
    #app.run(debug=app.config["DEBUG"], host="127.0.0.1", port=8082)