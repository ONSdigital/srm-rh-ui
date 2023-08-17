
import pytest

from rh_ui.controllers.rh_controller import get_uac_hash


def test_uac_hash(test_client):
    with pytest.raises(TypeError):
        get_uac_hash('Failed_uac')
