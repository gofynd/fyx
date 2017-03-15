# content of test_sample.py
from funcs import new_method


def func(x):
    print x
    return x + 1


def test_answer():
    y = new_method(2)
    assert func(y) == 4
