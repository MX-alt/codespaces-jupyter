import java.util.HashSet;
import java.util.Set;

public class _05RemoveDuplicateNodes {

    static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
    }

    // HashSet で訪問済みの値を管理し、重複ノードをスキップする
    public ListNode removeDuplicateNodes(ListNode head) {
        if (head == null) return null;

        Set<Integer> visited = new HashSet<>();
        visited.add(head.val);
        ListNode curr = head;

        while (curr != null && curr.next != null) {
            if (visited.contains(curr.next.val)) {
                curr.next = curr.next.next;
            } else {
                visited.add(curr.next.val);
                curr = curr.next;
            }
        }
        return head;
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

    static int[] toArray(ListNode head) {
        int size = 0;
        ListNode curr = head;
        while (curr != null) { size++; curr = curr.next; }
        int[] arr = new int[size];
        curr = head;
        for (int i = 0; i < size; i++) { arr[i] = curr.val; curr = curr.next; }
        return arr;
    }

    static boolean arrayEquals(int[] a, int[] b) {
        if (a.length != b.length) return false;
        for (int i = 0; i < a.length; i++) if (a[i] != b[i]) return false;
        return true;
    }

    public static void main(String[] args) {
        _05RemoveDuplicateNodes sol = new _05RemoveDuplicateNodes();

        // null head
        assert sol.removeDuplicateNodes(null) == null;

        // no duplicates
        assert arrayEquals(toArray(sol.removeDuplicateNodes(createList(1, 2, 3))), new int[]{1, 2, 3});

        // duplicates at end
        assert arrayEquals(toArray(sol.removeDuplicateNodes(createList(1, 2, 3, 3, 2, 1))), new int[]{1, 2, 3});

        // all same
        assert arrayEquals(toArray(sol.removeDuplicateNodes(createList(5, 5, 5))), new int[]{5});

        // single node
        assert arrayEquals(toArray(sol.removeDuplicateNodes(createList(7))), new int[]{7});

        System.out.println("All test cases passed ✅");
    }
}
