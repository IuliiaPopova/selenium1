import pytest

@pytest.fixture()
def set_up():
    print("Before every method")
    yield
    print("After")
