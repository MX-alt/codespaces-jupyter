class Solution:
    def waysToClimb(self, n: int) -> int:
        """计算爬 n 级台阶的方案数，每次可走 1、2 或 3 步。

        用滚动变量代替数组，空间 O(1)。
        状态转移：f(n) = f(n-1) + f(n-2) + f(n-3)
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 4

        a, b, c = 1, 2, 4   # f(1), f(2), f(3)
        for _ in range(n - 3):
            a, b, c = b, c, a + b + c
        return c


if __name__ == "__main__":
    s = Solution()

    # 边界：0 级或负数
    assert s.waysToClimb(0) == 0
    assert s.waysToClimb(-1) == 0

    # 基础用例
    assert s.waysToClimb(1) == 1   # {1}
    assert s.waysToClimb(2) == 2   # {1+1, 2}
    assert s.waysToClimb(3) == 4   # {1+1+1, 1+2, 2+1, 3}
    assert s.waysToClimb(4) == 7   # {1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1}

    # 较大值（递推验证）
    assert s.waysToClimb(5) == 13
    assert s.waysToClimb(10) == 274

    print("所有测试用例通过 ✅")
