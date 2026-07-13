public class _23OneEditDistance {

    public boolean oneEditAway(String first, String second) {
        int len1 = first.length();
        int len2 = second.length();

        if (len1 > len2) {
            return oneEditAway(second, first);
        }

        if (len2 - len1 > 1) {
            return false;
        }

        for (int i = 0; i < len1; i++) {
            if (first.charAt(i) != second.charAt(i)) {
                if (len1 == len2) {
                    return first.substring(i + 1).equals(second.substring(i + 1));
                } else {
                    return first.substring(i).equals(second.substring(i + 1));
                }
            }
        }

        return len2 - len1 <= 1;
    }

    public static void main(String[] args) {
        _23OneEditDistance sol = new _23OneEditDistance();

        assert sol.oneEditAway("pale", "ple") : "case 1 failed";
        assert sol.oneEditAway("pales", "pale") : "case 2 failed";
        assert sol.oneEditAway("pale", "bale") : "case 3 failed";
        assert !sol.oneEditAway("pale", "bake") : "case 4 failed";
        assert !sol.oneEditAway("a", "bb") : "case 5 failed";

        System.out.println("All test cases passed ✅");
    }
}
