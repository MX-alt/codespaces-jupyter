import java.util.ArrayList;
import java.util.List;

public class _09PalindromeLinkedList {

    static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
    }

    // ノード値を配列に収集し、双ポインタで両端から比較する
    public boolean isPalindrome(ListNode head) {
        List<Integer> vals = new ArrayList<>();
        ListNode curr = head;
        while (curr != null) {
            vals.add(curr.val);
            curr = curr.next;
        }

        int left = 0, right = vals.size() - 1;
        while (left < right) {
            if (!vals.get(left).equals(vals.get(right))) return false;
            left++;
            right--;
        }
        return true;
    }

    // ── 補助関数 ──────────────────────────────────────────────

    static ListNode createList(int... vals) {
        if (vals.length == 0) return null;
        ListNode head = new ListNode(vals[0]);
        ListNode curr = head;
        for (int i = 1; i < vals.length; i++) {
            curr.next = new ListNode(vals[i]);
            curr = curr.next;
        }
        return head;
    }

    public static void main(String[] args) {
        _09PalindromeLinkedList sol = new _09PalindromeLinkedList();

        assert sol.isPalindrome(null)                      == true  : "null → true";
        assert sol.isPalindrome(createList(7))             == true  : "[7] → true";
        assert sol.isPalindrome(createList(1, 2, 1))       == true  : "[1,2,1] → true";
        assert sol.isPalindrome(createList(1, 2, 2, 1))    == true  : "[1,2,2,1] → true";
        assert sol.isPalindrome(createList(1, 2, 3, 1))    == false : "[1,2,3,1] → false";
        assert sol.isPalindrome(createList(1, 2))          == false : "[1,2] → false";

        System.out.println("All test cases passed ✅");
    }
}
