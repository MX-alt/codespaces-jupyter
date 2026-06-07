import pytest

from helpers import load_py


mod = load_py("15-merge_in_place.py", "merge_in_place")


@pytest.mark.parametrize(
    ("nums1", "m", "nums2", "n", "expected"),
    [
        ([1, 3, 5, 0, 0, 0], 3, [2, 4, 6], 3, [1, 2, 3, 4, 5, 6]),
        ([1, 2, 3], 3, [], 0, [1, 2, 3]),
        ([0, 0, 0], 0, [1, 2, 3], 3, [1, 2, 3]),
        ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
        ([1, 2, 2, 0, 0], 3, [2, 3], 2, [1, 2, 2, 2, 3]),
        ([2, 0], 1, [1], 1, [1, 2]),
    ],
)
def test_merge(nums1, m, nums2, n, expected):
    mod.Solution().merge(nums1, m, nums2, n)

    assert nums1 == expected
