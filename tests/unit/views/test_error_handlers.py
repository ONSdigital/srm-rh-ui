def test_404_handled(test_client):
    response = test_client.get('/non-existent-endpoint')

    assert response.status_code == 404
