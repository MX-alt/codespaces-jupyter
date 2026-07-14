public class _19StringCompression {

    public String compressString(String s) {
        if (s == null) {
            throw new IllegalArgumentException("Input must not be null.");
        }
        if (s.isEmpty()) {
            return s;
        }

        StringBuilder compressed = new StringBuilder();
        int count = 1;

        for (int i = 1; i <= s.length(); i++) {
            if (i < s.length() && s.charAt(i) == s.charAt(i - 1)) {
                count++;
            } else {
                compressed.append(s.charAt(i - 1)).append(count);
                count = 1;
            }
        }

        String result = compressed.toString();
        return result.length() < s.length() ? result : s;
    }

    public static void main(String[] args) {
        _19StringCompression solution = new _19StringCompression();

        if (!"a2b1c5a3".equals(solution.compressString("aabcccccaaa"))) {
            throw new AssertionError("Case 1 failed");
        }
        if (!"abcd".equals(solution.compressString("abcd"))) {
            throw new AssertionError("Case 2 failed");
        }

        System.out.println("All test cases passed ✅");
    }
}
