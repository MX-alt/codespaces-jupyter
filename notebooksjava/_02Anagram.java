import java.util.Arrays;

public class _02Anagram {

    // 解法1：ソート法 — O(n log n) time, O(n) space
    public boolean isAnagramSort(String s1, String s2) {
        if (s1.length() != s2.length()) return false;
        char[] a = s1.toCharArray();
        char[] b = s2.toCharArray();
        Arrays.sort(a);
        Arrays.sort(b);
        return Arrays.equals(a, b);
    }

    // 解法2：カウント法 — O(n) time, O(1) space（英小文字限定）
    public boolean checkPermutation(String s1, String s2) {
        if (s1.length() != s2.length()) return false;

        int[] counts = new int[26];
        for (char c : s1.toCharArray()) counts[c - 'a']++;
        for (char c : s2.toCharArray()) counts[c - 'a']--;

        for (int count : counts) {
            if (count != 0) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        _02Anagram sol = new _02Anagram();

        // isAnagramSort
        assert sol.isAnagramSort("abc", "cba")   == true  : "abc/cba are anagrams";
        assert sol.isAnagramSort("apple", "pale") == false : "different lengths";
        assert sol.isAnagramSort("listen", "silent") == true;
        assert sol.isAnagramSort("hello", "world")   == false;

        // checkPermutation
        assert sol.checkPermutation("abc", "cba")      == true;
        assert sol.checkPermutation("apple", "pale")   == false;
        assert sol.checkPermutation("listen", "silent") == true;
        assert sol.checkPermutation("hello", "world")   == false;

        System.out.println("All test cases passed ✅");
    }
}
