# mymodule.py
def add(a, b):
    return a + b

# test_mymodule.py
import pytest

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2


# test_mymodule.py


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (-1, -1, -2),
    (0, 0, 0),
    (1, 10, 11),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
