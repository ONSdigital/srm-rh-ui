from rh_ui.create_app import create_app_object


app = create_app_object()

# Bind routes to app
from rh_ui import views
