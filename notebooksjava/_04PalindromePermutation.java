import java.util.HashSet;
import java.util.Set;

public class _04PalindromePermutation {

    // 集合の対消し法：奇数回出現する文字が 1 つ以下なら回文に並べ替え可能
    public boolean canPermutePalindrome(String s) {
        s = s.replace(" ", "").toLowerCase();
        Set<Character> oddChars = new HashSet<>();
        for (char c : s.toCharArray()) {
            if (!oddChars.add(c)) {
                oddChars.remove(c);
            }
        }
        return oddChars.size() <= 1;
    }

    public static void main(String[] args) {
        _04PalindromePermutation sol = new _04PalindromePermutation();

        assert sol.canPermutePalindrome("code")    == false : "code → false";
        assert sol.canPermutePalindrome("tactcoa") == true  : "tactcoa → true";
        assert sol.canPermutePalindrome("aab")     == true  : "aab → true";
        assert sol.canPermutePalindrome("a")       == true  : "single char → true";
        assert sol.canPermutePalindrome("")        == true  : "empty string → true";
        assert sol.canPermutePalindrome("Tact Coa") == true : "with spaces/uppercase → true";

        System.out.println("All test cases passed ✅");
    }
}
