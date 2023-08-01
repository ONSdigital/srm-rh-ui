from rh_ui.app import create_app

app = create_app()

# Bind routes to app
from rh_ui import views
