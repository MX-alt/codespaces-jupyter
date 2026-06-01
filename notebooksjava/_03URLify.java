public class _03URLify {

    // 解法1：双ポインタ法（後ろから操作）— O(n) time, O(1) extra space
    public String replaceSpaces(String chars, int trueLength) {
        char[] s = chars.toCharArray();
        int spaceCount = 0;
        for (int i = 0; i < trueLength; i++) {
            if (s[i] == ' ') spaceCount++;
        }

        int newIndex = trueLength + spaceCount * 2;

        for (int i = trueLength - 1; i >= 0; i--) {
            if (s[i] == ' ') {
                s[newIndex - 1] = '0';
                s[newIndex - 2] = '2';
                s[newIndex - 3] = '%';
                newIndex -= 3;
            } else {
                s[newIndex - 1] = s[i];
                newIndex--;
            }
        }
        return new String(s).trim();
    }

    // 解法2：Javaの組み込みメソッド — O(n) time, O(n) space
    public String replaceSpacesPythonic(String s, int trueLength) {
        return s.substring(0, trueLength).replace(" ", "%20");
    }

    public static void main(String[] args) {
        _03URLify sol = new _03URLify();

        // replaceSpaces（双ポインタ）
        // 末尾に spaceCount*2 分の余白が必要（Python 実装と同じ前提）
        assert sol.replaceSpaces("Mr John Smith    ", 13).equals("Mr%20John%20Smith") : "two spaces";
        assert sol.replaceSpaces("hello", 5).equals("hello")                          : "no spaces";
        assert sol.replaceSpaces("   ", 1).equals("%20")                              : "single space";

        // replaceSpacesPythonic
        assert sol.replaceSpacesPythonic("Mr John Smith    ", 13).equals("Mr%20John%20Smith");
        assert sol.replaceSpacesPythonic("hello", 5).equals("hello");
        assert sol.replaceSpacesPythonic("   ", 1).equals("%20");

        System.out.println("All test cases passed ✅");
    }
}
