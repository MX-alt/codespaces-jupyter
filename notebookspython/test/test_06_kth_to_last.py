import pytest

from helpers import load_py


mod = load_py("06-kth_to_last.py", "kth_to_last")


@pytest.mark.parametrize(
    ("values", "k", "expected"),
    [
        ([1, 2, 3, 4, 5], 2, 4),
        ([1, 2, 3, 4, 5], 1, 5),
        ([1, 2, 3, 4, 5], 5, 1),
        ([42], 1, 42),
    ],
)
def test_kth_to_last(values, k, expected):
    head = mod.create_linked_list(values)

    assert mod.Solution().kthToLast(head, k) == expected
