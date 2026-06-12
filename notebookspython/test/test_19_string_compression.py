import pytest

from helpers import load_py

mod = load_py("19-string-compression.py", "compress_string")

@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcd", "abcd"),
        ("a", "a"),
        ("aa", "aa"),
        ("aaa", "a3"),
        ("aab", "aab"),
        ("aaabbb", "a3b3"),
        ("aabbcc", "aabbcc"),
        ("aabcccc", "a2b1c4"),
        ("", ""),
    ],
)
def test_compress_string(s, expected):
    assert mod.compress_string(s) == expected
