import pytest

def inc(x):
    return x + 1

@pytest.mark.search
def test_answer():
    assert inc(3) == 4