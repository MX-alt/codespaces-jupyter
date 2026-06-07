import pytest

from helpers import load_py


mod = load_py("02-anagram.py", "anagram")


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        ("abc", "cba", True),
        ("apple", "pale", False),
        ("listen", "silent", True),
        ("aabbcc", "abcabc", True),
        ("abc", "ab", False),
    ],
)
def test_is_anagram_sort(left, right, expected):
    assert mod.is_anagram_sort(left, right) is expected


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        ("abc", "cba", True),
        ("apple", "pale", False),
        ("listen", "silent", True),
        ("aabbcc", "abcabc", True),
        ("abc", "ab", False),
    ],
)
def test_check_permutation(left, right, expected):
    assert mod.CheckPermutation(left, right) is expected
