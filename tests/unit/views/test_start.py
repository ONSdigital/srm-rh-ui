from unittest.mock import patch, Mock

from requests import HTTPError


def test_en_start_endpoint_success(test_client):
    response = test_client.get('/en/start', follow_redirects=True)

    assert response.status_code == 200
    assert '<div class="ons-header__title">ONS Surveys</div>'.encode() in response.data
    assert 'Enter your 16-character access code'.encode() in response.data


def test_cy_start_endpoint_success(test_client):
    response = test_client.get('/cy/start', follow_redirects=True)

    assert response.status_code == 200
    assert "Arolygon SYG".encode() in response.data
    assert "Rhowch eich cod mynediad sy'n cynnwys 16 o nodau".encode() in response.data


def test_en_enter_uac_success(test_client):
    with patch('rh_ui.controllers.rh_controller.requests.get') as mock_get:
        mock_get.return_value.text = 'MOCKEQTOKEN'
        response = test_client.post('/en/start/', data={"access-code": "1234567890123456"})

    assert response.status_code == 302
    assert response.location == 'http://localhost:5000/session?token=MOCKEQTOKEN'


def test_en_enter_uac_blank(test_client):
    response = test_client.post('/en/start/', data={"access-code": ""}, follow_redirects=True)

    assert response.status_code == 200
    assert 'Enter an access code'.encode() in response.data


def test_en_enter_uac_invalid_length(test_client):
    response = test_client.post('/en/start/', data={"access-code": "testing"}, follow_redirects=True)

    assert response.status_code == 200
    assert 'Enter a 16-character access code'.encode() in response.data


def test_en_enter_uac_inactive(test_client):
    mock = Mock()
    mock.text = 'UAC_INACTIVE'
    mock.status_code = 400

    with patch('rh_ui.controllers.rh_controller.requests.get') as mock_get:
        mock_get.return_value.raise_for_status.side_effect = HTTPError(response=mock)

        response = test_client.post('/en/start/', data={"access-code": "1234567890123456"})
    assert response.status_code == 200
    assert 'This questionnaire has now closed' in response.text


def test_en_enter_uac_receipted(test_client):
    mock = Mock()
    mock.text = 'UAC_RECEIPTED'
    mock.status_code = 400

    with patch('rh_ui.controllers.rh_controller.requests.get') as mock_get:
        mock_get.return_value.raise_for_status.side_effect = HTTPError(response=mock)

        response = test_client.post('/en/start/', data={"access-code": "1234567890123456"})
    assert response.status_code == 200
    assert 'This access code has already been used' in response.text


def test_en_enter_uac_not_found(test_client):
    mock = Mock()
    mock.status_code = 404

    with patch('rh_ui.controllers.rh_controller.requests.get') as mock_get:
        mock_get.return_value.raise_for_status.side_effect = HTTPError(response=mock)

        response = test_client.post('/en/start/', data={"access-code": "1234567890123456"}, follow_redirects=True)
    assert response.status_code == 200
    assert 'Access code not recognised. Enter the code again.' in response.text
