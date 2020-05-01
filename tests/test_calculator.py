import multiples_of_x_and_y.calculator as calculator
import pytest


@pytest.mark.parametrize("x,y,goal,expected", [
    (3, 5, 10, (3, 5, 6, 9)),
    (5, 9, 20, (5, 9, 10, 15, 18)),
    (1, 2, 3, (1, 2))
])
def test_calculate(x, y, goal, expected):
    actual = calculator.calculate(x, y, goal)
    assert actual == expected

@pytest.mark.parametrize("divider,dividend,expected", [
        (1, 1, True),
        (2, 1, False),
        (2, 2, True),
        (2, 3, False),
        (576576, 6354, False),
        (676, 7364780, False),
    ])
def test_can_divide(divider, dividend, expected):
    actual = calculator.can_divide(divider, dividend)
    assert actual == expected