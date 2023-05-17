import pytest

@pytest.fixture(params=[['tom',123],['jerry',456],['linda',789]],
                ids=['tom','jerry','linda'])
def login(request):
    return request.param

def test_login(login):
    print(login)