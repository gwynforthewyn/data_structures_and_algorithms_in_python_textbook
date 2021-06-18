import pytest

from chapone import reinforcement


# Write a short Python function, is_multiple(n, m),
# that takes two integer values and returns True if
# n is a multiple of m, that is, n = mi for some integer
# i, and False otherwise.
@pytest.mark.parametrize(
    "n_,m_,result_",
    [
        (0, 0, False),
        (1, 1, True),
        (12, 3, True),
        (15, 7, False),
        (-10, -5, True),
        (-10, -6, False)
    ]
    )
def test_one(n_, m_, result_):
  assert reinforcement.is_multiple(n_, m_) == result_


# Write a short Python function, is_even(k),
# that takes an integer value and returns
# True if k is even, and False otherwise.
# However, your function cannot use the
# multiplication, modulo, or division operators.
@pytest.mark.parametrize(
    "k_,result_",
    [
        (2, True),
        (3, False),
        (4, True),
        (17, False),
        (21345, False),
        (12348, True),
        ("foo", False)
    ]
    )
def test_two(k_, result_):
    assert reinforcement.is_even(k_) == result_

# Write a short Python function, minmax(data), that
# takes a sequence of one or more numbers, and returns
# the smallest and largest numbers, in the form of a
# tuple of length two. Do not use the built-in functions
# min or max in implementing your solution.
@pytest.mark.parametrize(
    "input_,result_",
    [
        ((1, 2), (1, 2)),
        ((1, 2, 3), (1, 3)),
    ]
    )
def test_three(input_, result_):
    assert reinforcement.minmax(input_) == result_


# Write a short Python function that takes
# a positive integer n and returns the sum of the
# squares of all the positive integers smaller than n.
@pytest.mark.parametrize(
    "input_,result_",
    [
        (1, 0),
        (4, 14),
        (10, 285)
    ]
    )
def test_four(input_, result_):
    assert reinforcement.sum_of_squares(input_) == result_


# Write a short Python function that takes a positive
# integer n and returns the sum of the squares of all
# the odd positive integers smaller than n.
@pytest.mark.parametrize(
    "input_,result_",
    [
        (1, 0),
        (4, 10),
        (10, 165)
    ]
    )
def test_four(input_, result_):
    assert reinforcement.sum_of_odd_squares(input_) == result_
