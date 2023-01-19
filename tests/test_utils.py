from unittest import mock
from unittest.mock import Mock

from wagwan.utils import *


@mock.patch("os.path.isfile")
def test_path_exists(mock_os_path_isfile):
    mock_os_path_isfile.return_value = Mock(output=True)
    response = path_exists()
    assert response.output is True


@mock.patch("typer.prompt")
def test_get_key(mock_typer_prompt):
    mock_typer_prompt.return_value = Mock(key="API_KEY")
    response = get_key()
    assert response.key is not None
    assert response.key == "API_KEY"
