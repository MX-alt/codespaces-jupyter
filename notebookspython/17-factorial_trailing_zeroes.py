class Solution:
    def trailingZeroes(self, n: int) -> int:
        """Return how many trailing zeroes are in n!.

        A trailing zero comes from a factor pair 2 * 5. Factor 2 is always
        more common than factor 5, so count how many 5s appear in n!.
        """
        count = 0

        while n > 0:
            n //= 5
            count += n

        return count


if __name__ == "__main__":
    sol = Solution()

    # Case 1: 3! = 6, no trailing zero
    assert sol.trailingZeroes(3) == 0

    # Case 2: 5! = 120, one trailing zero
    assert sol.trailingZeroes(5) == 1

    # Case 3: 10! = 3628800, two trailing zeroes
    assert sol.trailingZeroes(10) == 2

    # Case 4: 25 contributes 5 and 25, so 25! has six trailing zeroes
    assert sol.trailingZeroes(25) == 6

    # Case 5: 125 contributes an extra layer of factor 5
    assert sol.trailingZeroes(125) == 31

    # Case 6: zero factorial is 1, no trailing zero
    assert sol.trailingZeroes(0) == 0

    print("All test cases passed ✅")
