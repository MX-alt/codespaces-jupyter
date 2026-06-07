import pytest

from helpers import load_py


mod = load_py("09-palindrome_linked_list.py", "palindrome_linked_list")


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([], True),
        ([7], True),
        ([1, 2, 1], True),
        ([1, 2, 2, 1], True),
        ([1, 2, 3, 1], False),
        ([1, 2], False),
    ],
)
def test_is_palindrome(values, expected):
    head = mod.create_linked_list(values)

    assert mod.Solution().isPalindrome(head) is expected
