public class _20StringRotation {

    public boolean isFlippedString(String s1, String s2) {
        if (s1 == null || s2 == null) {
            throw new IllegalArgumentException("Inputs must not be null.");
        }
        if (s1.length() != s2.length()) {
            return false;
        }
        if (s1.isEmpty()) {
            return true;
        }

        return (s1 + s1).contains(s2);
    }

    public static void main(String[] args) {
        _20StringRotation solution = new _20StringRotation();

        if (!solution.isFlippedString("waterbottle", "erbottlewat")) {
            throw new AssertionError("Case 1 failed");
        }
        if (!solution.isFlippedString("abcde", "cdeab")) {
            throw new AssertionError("Case 2 failed");
        }
        if (solution.isFlippedString("abcde", "abced")) {
            throw new AssertionError("Case 3 failed");
        }
        if (!solution.isFlippedString("", "")) {
            throw new AssertionError("Case 4 failed");
        }

        System.out.println("All test cases passed ✅");
    }
}
