from rh_ui import app
from rh_ui.views.hello import hello_bp

app.register_blueprint(hello_bp, url_prefix="/")
