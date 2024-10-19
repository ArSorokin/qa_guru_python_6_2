import pytest


@pytest.fixture()
def user_id():
    return 123


@pytest.fixture()
def my_chrome(browser_open):
    print('Chrome стартует')
    yield
    print('Chrome закрывается')


def test_auth(user_id, my_chrome):
    assert user_id == 123


# def test_second(user_id, chrome):
#     assert user_id == 123


# def test_third(user_id, chrome):
#     assert user_id == 123
