import pytest
from chapone import vowels as v

# Write a short Python function, is_multiple(n, m),
# that takes two integer values and returns True if
# n is a multiple of m, that is, n = mi for some integer
# i, and False otherwise.
@pytest.mark.parametrize(
    "string_,result_",
    [
        ("l", 0),
        ("lol", 1),
        ("The grand old DUKE of YORK", 7),
    ]
    )
def test_one(string_, result_):
  assert v.count_vowels(string_) == result_
