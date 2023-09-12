import pytest

from rh_ui.app_setup import create_app
from tests.integration.utilities import populate_database, populate_firestore, truncate_database


@pytest.fixture
def app():
    app = create_app()
    return app


@pytest.fixture
def test_client(app):
    test_client = app.test_client()
    with app.app_context():
        yield test_client


@pytest.fixture(scope="session")
def setup_data():
    populate_database()
    populate_firestore()
    yield
    truncate_database()
