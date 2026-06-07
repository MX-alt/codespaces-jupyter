import pytest

from helpers import load_py


mod = load_py("04-palindrome_permutation.py", "palindrome_permutation")


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("code", False),
        ("tactcoa", True),
        ("Tact Coa", True),
        ("aabb", True),
        ("abc", False),
        ("", True),
    ],
)
def test_can_permute_palindrome(text, expected):
    assert mod.Solution().canPermutePalindrome(text) is expected
