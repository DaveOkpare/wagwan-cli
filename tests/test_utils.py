from unittest import mock
from unittest.mock import Mock

from wagwan.utils import *


@mock.patch("os.path.isfile", Mock(return_value=True))
def test_path_exists():
    response = path_exists()
    assert response is True


@mock.patch("typer.prompt", Mock(return_value="API_KEY"))
def test_get_key():
    response = get_key()
    assert response is not None
    assert response == "API_KEY"


# @mock.patch()
# @mock.patch("typing.IO.readlines", Mock(return_value="OUTPUT_STRING"))
# def test_read_file():
#     response = OpenAI(file_path="~/temp").read_file()
#     assert response is not None

@mock.patch("wagwan.utils.OpenAI.read_file", Mock(return_value="This is output text"))
def test_explain_prompt():
    response = OpenAI(file_path="~/temp").explain_prompt()
    assert response is not None
