import pytest

from helpers import load_ipynb


mod = load_ipynb("01-is-unique.ipynb", "is_unique")


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
