import pytest

from helpers import load_py


mod = load_py("17-factorial_trailing_zeroes.py", "factorial_trailing_zeroes")


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (0, 0),
        (3, 0),
        (5, 1),
        (10, 2),
        (25, 6),
        (125, 31),
    ],
)
def test_trailing_zeroes(n, expected):
    assert mod.Solution().trailingZeroes(n) == expected
