import pytest
import chapone.creativity

@pytest.mark.parametrize(
    "input_,result_",
    [
        ([1, 2], False),
        ([2, 2], False),
        ([1, 2, 3, 4, 5], True),
    ]
    )
def test_distinct_pairs_generate_odd_number(input_, result_):
    assert chapone.creativity.distinct_pairs_generate_odd_number(input_) == result_
