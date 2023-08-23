from unittest.mock import patch, Mock

import pytest

from rh_ui.controllers.rh_service import get_uac_hash, get_eq_token


@pytest.mark.parametrize(
    'uac',
    ('',
     'SHORTUAC',
     'UACTHATISTOOLONGWITHTOOMANYCHARACTERS',
     'BADCHARS1234*&^%')
)
def test_uac_hash_errors_on_bad_uac_format(uac):
    # When we try to hash a UAC that is an invalid format, then it raises the error
    with pytest.raises(TypeError):
        get_uac_hash('Failed_uac')


def test_uac_hash():
    # When we try to hash a 16 char UAC
    uac_hash = get_uac_hash('EXAMPLEUAC121234')

    # Then we get a hash back
    assert isinstance(uac_hash, str), 'UAC hash should be a string'
    assert uac_hash, 'UAC hash should be none zero length'


def test_get_eq_token(test_client):
    mock_response = Mock()
    mock_response.text = 'MOCK_EQ_TOKEN_RESPONSE'
    with patch('rh_ui.controllers.rh_service.requests.get') as mock_get:
        mock_get.return_value = mock_response
        response = get_eq_token('ABCD1234ABCD1234', 'en')

    assert response.text == mock_response.text, 'Expect the response text to the returned'
