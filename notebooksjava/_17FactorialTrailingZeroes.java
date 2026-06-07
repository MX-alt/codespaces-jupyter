public class _17FactorialTrailingZeroes {

    public int trailingZeroes(int n) {
        int count = 0;

        // 末尾 0 来自 2 * 5；2 一定更充足，所以只统计 n! 中因子 5 的数量
        while (n > 0) {
            n /= 5;
            count += n;
        }

        return count;
    }

    public static void main(String[] args) {
        _17FactorialTrailingZeroes sol = new _17FactorialTrailingZeroes();

        // Case 1: 3! = 6，没有末尾 0
        assert sol.trailingZeroes(3) == 0 : "case 1 failed";

        // Case 2: 5! = 120，有 1 个末尾 0
        assert sol.trailingZeroes(5) == 1 : "case 2 failed";

        // Case 3: 10! = 3628800，有 2 个末尾 0
        assert sol.trailingZeroes(10) == 2 : "case 3 failed";

        // Case 4: 25 会额外贡献一次因子 5，所以 25! 有 6 个末尾 0
        assert sol.trailingZeroes(25) == 6 : "case 4 failed";

        // Case 5: 125 会再额外贡献一层因子 5
        assert sol.trailingZeroes(125) == 31 : "case 5 failed";

        // Case 6: 0! = 1，没有末尾 0
        assert sol.trailingZeroes(0) == 0 : "case 6 failed";

        System.out.println("All test cases passed ✅");
    }
}
