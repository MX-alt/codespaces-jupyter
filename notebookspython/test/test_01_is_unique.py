import pytest

from helpers import load_py


mod = load_py("01-is-unique.py", "is_unique")


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("abc", True),
        ("leetcode", False),
        ("algorithm", True),
        ("hello", False),
        ("", True),
    ],
)
def test_is_unique(text, expected):
    assert mod.Solution().isUnique(text) is expected
