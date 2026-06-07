import pytest

from helpers import load_ipynb


mod = load_ipynb("03-urlify.ipynb", "urlify")


@pytest.mark.parametrize(
    ("chars", "true_length", "expected"),
    [
        ("Mr John Smith    ", 13, "Mr%20John%20Smith"),
        ("a b  ", 3, "a%20b"),
        ("abc", 3, "abc"),
    ],
)
def test_replace_spaces(chars, true_length, expected):
    assert mod.Solution().replaceSpaces(chars, true_length) == expected


@pytest.mark.parametrize(
    ("chars", "true_length", "expected"),
    [
        ("Mr John Smith    ", 13, "Mr%20John%20Smith"),
        ("a b  ", 3, "a%20b"),
        ("abc", 3, "abc"),
    ],
)
def test_urlify_pythonic(chars, true_length, expected):
    assert mod.urlify_pythonic(chars, true_length) == expected
