public class _18AddWithoutArithmetic {

    public int add(int a, int b) {
        // 用异或合并无进位结果，用与和左移计算进位。
        while (b != 0) {
            int carry = (a & b) << 1;
            a = a ^ b;
            b = carry;
        }

        return a;
    }

    public static void main(String[] args) {
        _18AddWithoutArithmetic sol = new _18AddWithoutArithmetic();

        // Case 1: 两个正数
        assert sol.add(1, 2) == 3 : "case 1 failed";

        // Case 2: 0 不改变另一个值
        assert sol.add(5, 0) == 5 : "case 2 failed";

        // Case 3: 符号相反时相互抵消
        assert sol.add(-1, 1) == 0 : "case 3 failed";

        // Case 4: 两个负数
        assert sol.add(-3, -4) == -7 : "case 4 failed";

        // Case 5: 较大的正数
        assert sol.add(123, 456) == 579 : "case 5 failed";

        // Case 6: 遵循 Java int 溢出行为
        assert sol.add(0x7fffffff, 1) == 0x80000000 : "case 6 failed";

        System.out.println("All test cases passed ✅");
    }
}
