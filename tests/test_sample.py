import pytest

def test_expected_error():
    with pytest.raises(TypeError):
        assert 1 + "a", "This should raise an error"