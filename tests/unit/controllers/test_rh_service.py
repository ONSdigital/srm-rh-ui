import pytest

from rh_ui.controllers.rh_service import get_uac_hash


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
