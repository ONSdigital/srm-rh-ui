def test_hello_endpoint_success(test_client):
    response = test_client.get('/hello')

    assert response.status_code == 200
    assert "<title>Title: Hello World!</title>".encode() in response.data
    assert "<h1>Hello, World!</h1>".encode() in response.data
