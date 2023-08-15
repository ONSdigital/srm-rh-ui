def test_en_start_endpoint_success(test_client):
    response = test_client.get('/en/start', follow_redirects=True)

    assert response.status_code == 200
    assert '<div class="ons-header__title">ONS Surveys</div>'.encode() in response.data
    assert 'Enter your 16-character access code'.encode() in response.data


def test_cy_start_endpoint_success(test_client):
    response = test_client.get('/cy/start', follow_redirects=True)

    assert response.status_code == 200
    assert '<div class="ons-header__title">ONS Surveys</div>'.encode() in response.data
    assert 'PLACEHOLDER WELSH Enter your 16-character access code'.encode() in response.data


def test_en_enter_uac_success(test_client):
    response = test_client.post('/en/start/', data={"access-code": "1234567890123456"}, follow_redirects=True)

    assert response.status_code == 200


def test_en_enter_uac_blank(test_client):
    response = test_client.post('/en/start/', data={"access-code": ""}, follow_redirects=True)

    assert response.status_code == 200
    assert 'Enter an access code'.encode() in response.data


def test_en_enter_uac_invalid_length(test_client):
    response = test_client.post('/en/start/', data={"access-code": "testing"}, follow_redirects=True)

    assert response.status_code == 200
    assert 'Enter a 16-character access code'.encode() in response.data


def test_404_page(test_client):
    response = test_client.get('/invalid/')

    assert 'Page not found'.encode() in response.data
