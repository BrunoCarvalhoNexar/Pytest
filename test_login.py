import pytest


def testLogin():
    print("Login Succesful")
def testLogoff():
    print("Logoff Succesful")
#this skip a test or method
@pytest.mark.xfail
def testCalculation():
    assert 2+2 == 5