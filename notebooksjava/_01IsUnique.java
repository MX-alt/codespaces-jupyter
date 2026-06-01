import java.util.HashSet;
import java.util.Set;

public class _01IsUnique {

    // 解法1：HashSet — O(n) time, O(n) space
    public boolean isUnique(String astr) {
        Set<Character> seen = new HashSet<>();
        for (char c : astr.toCharArray()) {
            if (!seen.add(c)) return false;
        }
        return true;
    }

    // 解法2：ビット演算 — O(n) time, O(1) space（a-z のみ対応）
    public boolean isUniqueBit(String astr) {
        int mark = 0;
        for (char c : astr.toCharArray()) {
            int bit = c - 'a';
            if ((mark & (1 << bit)) != 0) return false;
            mark |= (1 << bit);
        }
        return true;
    }

    public static void main(String[] args) {
        _01IsUnique sol = new _01IsUnique();

        // isUnique
        assert sol.isUnique("abc")      == true  : "abc should be unique";
        assert sol.isUnique("apple")    == false : "apple has duplicate 'p'";
        assert sol.isUnique("")         == true  : "empty string is unique";
        assert sol.isUnique("a")        == true  : "single char is unique";
        assert sol.isUnique("leetcode") == false : "leetcode has duplicates";

        // isUniqueBit
        assert sol.isUniqueBit("abc")      == true  : "abc should be unique (bit)";
        assert sol.isUniqueBit("apple")    == false : "apple has duplicate 'p' (bit)";
        assert sol.isUniqueBit("leetcode") == false : "leetcode has duplicates (bit)";

        System.out.println("All test cases passed ✅");
    }
}
