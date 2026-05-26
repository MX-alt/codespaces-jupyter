class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """Merge nums2 into nums1 in-place, both arrays are sorted.

        nums1 has length m + n, where the last n slots are empty (0-padded).
        Fill from the back to avoid overwriting unprocessed elements.
        """
        i = m - 1       # last real element in nums1
        j = n - 1       # last element in nums2
        k = m + n - 1   # write position (back of nums1)

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # Any remaining elements in nums2 still need to be copied;
        # remaining elements in nums1 are already in place.
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


if __name__ == "__main__":
    s = Solution()

    # Case 1: standard merge, unequal lengths
    a = [1, 3, 5, 0, 0, 0]
    s.merge(a, 3, [2, 4, 6], 3)
    assert a == [1, 2, 3, 4, 5, 6]

    # Case 2: nums2 is empty — nums1 unchanged
    a = [1, 2, 3]
    s.merge(a, 3, [], 0)
    assert a == [1, 2, 3]

    # Case 3: nums1 is empty — result is nums2
    a = [0, 0, 0]
    s.merge(a, 0, [1, 2, 3], 3)
    assert a == [1, 2, 3]

    # Case 4: all of nums2 is smaller than nums1
    a = [4, 5, 6, 0, 0, 0]
    s.merge(a, 3, [1, 2, 3], 3)
    assert a == [1, 2, 3, 4, 5, 6]

    # Case 5: arrays with duplicate values
    a = [1, 2, 2, 0, 0]
    s.merge(a, 3, [2, 3], 2)
    assert a == [1, 2, 2, 2, 3]

    # Case 6: single-element arrays
    a = [2, 0]
    s.merge(a, 1, [1], 1)
    assert a == [1, 2]

    print("All test cases passed ✅")
