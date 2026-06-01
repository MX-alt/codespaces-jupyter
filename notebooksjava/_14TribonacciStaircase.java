public class _14TribonacciStaircase {

    // 滚动变量代替数组，空间 O(1)
    // 状态转移：f(n) = f(n-1) + f(n-2) + f(n-3)
    public int waysToClimb(int n) {
        if (n <= 0) return 0;
        if (n == 1) return 1;
        if (n == 2) return 2;
        if (n == 3) return 4;

        int a = 1, b = 2, c = 4;
        for (int i = 0; i < n - 3; i++) {
            int next = a + b + c;
            a = b;
            b = c;
            c = next;
        }
        return c;
    }

    public static void main(String[] args) {
        _14TribonacciStaircase sol = new _14TribonacciStaircase();

        // 境界値
        assert sol.waysToClimb(0)  == 0  : "n=0 → 0";
        assert sol.waysToClimb(-1) == 0  : "n=-1 → 0";

        // 基本用例
        assert sol.waysToClimb(1)  == 1  : "n=1 → 1";
        assert sol.waysToClimb(2)  == 2  : "n=2 → 2";
        assert sol.waysToClimb(3)  == 4  : "n=3 → 4";
        assert sol.waysToClimb(4)  == 7  : "n=4 → 7";
        assert sol.waysToClimb(5)  == 13 : "n=5 → 13";
        assert sol.waysToClimb(10) == 274 : "n=10 → 274";

        System.out.println("All test cases passed ✅");
    }
}
