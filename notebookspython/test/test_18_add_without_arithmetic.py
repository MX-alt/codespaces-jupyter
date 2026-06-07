import pytest

from helpers import load_py


mod = load_py("18-add_without_arithmetic.py", "add_without_arithmetic")


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (1, 2, 3),
        (5, 0, 5),
        (-1, 1, 0),
        (-3, -4, -7),
        (123, 456, 579),
        (0x7FFFFFFF, 1, -0x80000000),
    ],
)
def test_add(a, b, expected):
    assert mod.Solution().add(a, b) == expected
