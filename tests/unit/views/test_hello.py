from rh_ui import app


def test_cookies_success():
    test_client = app.test_client()

    response = test_client.get('/')

    assert response.status_code == 200
    assert "<title>Title: Hello World!</title>".encode() in response.data
    assert "<h1>Hello, World!</h1>".encode() in response.data
