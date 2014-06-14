#
from canariya import test_config


@test_config(target=object())
def test_it1():
    """ dummy test 1 """
    pass


@test_config(target=object())
def test_it2():
    """ dummy test 2 """
    assert False, "dummy failure"


@test_config(target=object(),
    values=[
        {"var1": 1, "var2": 2, "expected": 3},
        {"var1": 2, "var2": 4, "expected": 6},
        {"var1": 2, "var2": 4, "expected": 8},
    ],
    description="test for add values:{values}")
def test_add(var1, var2, expected):
    """ test for add """
    assert var1 + var2 == expected