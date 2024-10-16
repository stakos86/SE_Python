import pytest
from main import hello_world


def test_hello_world():
    sample = True
    result = hello_world()
    assert sample == result
