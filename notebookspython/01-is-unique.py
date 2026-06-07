class SolutionSet:
    def isUnique(self, astr: str) -> bool:
        return len(astr) == len(set(astr))


class Solution:
    def isUnique(self, astr: str) -> bool:
        """Check uniqueness for lowercase a-z characters using a bit mask."""
        mark = 0

        for char in astr:
            move_bit = ord(char) - ord("a")
            if (mark & (1 << move_bit)) != 0:
                return False
            mark |= 1 << move_bit

        return True


if __name__ == "__main__":
    sol = Solution()

    assert sol.isUnique("abc") is True
    assert sol.isUnique("leetcode") is False
    assert sol.isUnique("algorithm") is True
    assert sol.isUnique("hello") is False
    assert sol.isUnique("") is True

    print("All test cases passed ✅")
