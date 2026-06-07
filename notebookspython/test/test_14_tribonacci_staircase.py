import pytest

from helpers import load_py


mod = load_py("14-tribonacci_staircase.py", "tribonacci_staircase")


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (0, 0),
        (-1, 0),
        (1, 1),
        (2, 2),
        (3, 4),
        (4, 7),
        (5, 13),
        (10, 274),
    ],
)
def test_ways_to_climb(n, expected):
    assert mod.Solution().waysToClimb(n) == expected
