public class _06KthToLast {

    static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
    }

    // 快慢指针：fast 先走 k 步，然后两指针同步前进直到 fast 为 null
    public int kthToLast(ListNode head, int k) {
        ListNode fast = head;
        ListNode slow = head;

        for (int i = 0; i < k; i++) {
            fast = fast.next;
        }

        while (fast != null) {
            fast = fast.next;
            slow = slow.next;
        }

        return slow.val;
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
        _06KthToLast sol = new _06KthToLast();

        ListNode head = createList(1, 2, 3, 4, 5);

        assert sol.kthToLast(head, 1) == 5 : "倒数第1个应为5";
        assert sol.kthToLast(head, 2) == 4 : "倒数第2个应为4";
        assert sol.kthToLast(head, 3) == 3 : "倒数第3个应为3";
        assert sol.kthToLast(head, 5) == 1 : "倒数第5个应为1";

        // 单节点链表
        assert sol.kthToLast(createList(42), 1) == 42;

        System.out.println("All test cases passed ✅");
    }
}
