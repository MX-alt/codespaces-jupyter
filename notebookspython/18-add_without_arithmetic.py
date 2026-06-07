class Solution:
    def add(self, a: int, b: int) -> int:
        """Add two 32-bit signed integers using bit operations only."""
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        if a <= max_int:
            return a
        return ~(a ^ mask)


if __name__ == "__main__":
    sol = Solution()

    # Case 1: two positive numbers
    assert sol.add(1, 2) == 3

    # Case 2: zero keeps the other value unchanged
    assert sol.add(5, 0) == 5

    # Case 3: opposite signs cancel out
    assert sol.add(-1, 1) == 0

    # Case 4: two negative numbers
    assert sol.add(-3, -4) == -7

    # Case 5: larger positive numbers
    assert sol.add(123, 456) == 579

    # Case 6: follows 32-bit signed integer overflow behavior
    assert sol.add(0x7FFFFFFF, 1) == -0x80000000

    print("All test cases passed ✅")
