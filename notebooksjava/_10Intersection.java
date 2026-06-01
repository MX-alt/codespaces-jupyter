import java.util.HashSet;
import java.util.Set;

public class _10Intersection {

    static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
    }

    // 解法1：HashSet — O(m+n) time, O(m) space
    public ListNode getIntersectionNodeSet(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) return null;

        Set<ListNode> seen = new HashSet<>();
        ListNode curr = headA;
        while (curr != null) { seen.add(curr); curr = curr.next; }

        curr = headB;
        while (curr != null) {
            if (seen.contains(curr)) return curr;
            curr = curr.next;
        }
        return null;
    }

    // 解法2：双ポインタ対齐法 — O(m+n) time, O(1) space
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) return null;

        ListNode a = headA, b = headB;
        while (a != b) {
            a = (a == null) ? headB : a.next;
            b = (b == null) ? headA : b.next;
        }
        return a;
    }

    // ── 補助関数 ──────────────────────────────────────────────

    static ListNode buildSharedTail(int... vals) {
        if (vals.length == 0) return null;
        ListNode head = new ListNode(vals[0]);
        ListNode curr = head;
        for (int i = 1; i < vals.length; i++) {
            curr.next = new ListNode(vals[i]);
            curr = curr.next;
        }
        return head;
    }

    static ListNode buildPrefix(ListNode tail, int... vals) {
        if (vals.length == 0) return tail;
        ListNode head = new ListNode(vals[0]);
        ListNode curr = head;
        for (int i = 1; i < vals.length; i++) {
            curr.next = new ListNode(vals[i]);
            curr = curr.next;
        }
        curr.next = tail;
        return head;
    }

    public static void main(String[] args) {
        _10Intersection sol = new _10Intersection();

        // 両方 null → null
        assert sol.getIntersectionNode(null, null) == null;
        assert sol.getIntersectionNodeSet(null, null) == null;

        // 片方 null → null
        ListNode single = new ListNode(1);
        assert sol.getIntersectionNode(null, single) == null;
        assert sol.getIntersectionNode(single, null) == null;

        // 相交ノードあり
        ListNode shared = buildSharedTail(8, 4, 5);
        ListNode headA  = buildPrefix(shared, 4, 1);
        ListNode headB  = buildPrefix(shared, 5, 6, 1);

        assert sol.getIntersectionNode(headA, headB)    == shared : "two-pointer should find intersection";
        assert sol.getIntersectionNodeSet(headA, headB) == shared : "set should find intersection";

        // 完全共有（先頭で相交）
        assert sol.getIntersectionNode(shared, shared) == shared;

        // 相交なし
        ListNode c = buildSharedTail(1, 2, 3);
        ListNode d = buildSharedTail(4, 5, 6);
        assert sol.getIntersectionNode(c, d) == null;

        System.out.println("All test cases passed ✅");
    }
}
