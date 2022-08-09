from datetime import datetime
from example import hi, bye, how_are_you
import pytest


@pytest.fixture
def bob():
    return {"name": "Bob"}


@pytest.fixture
def jane():
    return {"name": "Jane", "DOB" : "01/01/1980"}


def test_hello(jane):
    assert hi(jane) == "Hi, Jane"


def test_bye(bob):
    assert bye(bob) == "Bye, Bob"


def test_how_are_you(bob):
    assert how_are_you(bob) == "How are you Bob?"
