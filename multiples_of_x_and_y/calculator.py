
MIN_GOAL = 1

def calculate(x, y, goal):
    assert x > 0
    assert y > 0
    assert goal >= MIN_GOAL
    range_numbers = range(MIN_GOAL, goal)
    condition = as_condition(x, y)
    filtered_numbers = filter(condition, range_numbers)
    return tuple(filtered_numbers)

def as_condition(x, y):
    assert x > 0
    assert y > 0
    selector = lambda value: can_divide(x, value) | can_divide(y, value)
    return selector

def can_divide(divider, dividend):
    assert divider > 0
    assert dividend > 0
    return dividend % divider == 0
