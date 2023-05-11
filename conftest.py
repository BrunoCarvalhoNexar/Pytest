import pytest


@pytest.fixture(scope="session",autouse=True)
def tc_setup():
    print("Launch browser")
    print("Login")
    print("Browse products")
    #tear down
    yield
    print("Logoff")
    print("Close Browser")