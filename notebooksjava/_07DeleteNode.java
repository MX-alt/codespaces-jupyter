public class _07DeleteNode {

    static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
    }

    // 次のノードの値をコピーして next を飛ばすことで、head なしで削除を実現する
    public void deleteNode(ListNode node) {
        node.val  = node.next.val;
        node.next = node.next.next;
    }

    // ── 補助関数 ──────────────────────────────────────────────

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
        _07DeleteNode sol = new _07DeleteNode();

        // 4 -> 5 -> 1 -> 9、ノード5を削除 → 4 -> 1 -> 9
        ListNode head = new ListNode(4);
        ListNode nodeToDelete = new ListNode(5);
        head.next = nodeToDelete;
        head.next.next = new ListNode(1);
        head.next.next.next = new ListNode(9);

        sol.deleteNode(nodeToDelete);
        assert arrayEquals(toArray(head), new int[]{4, 1, 9}) : "should be [4,1,9]";

        // 先頭以外の中間ノードを削除
        ListNode h2 = new ListNode(1);
        ListNode mid = new ListNode(2);
        h2.next = mid;
        h2.next.next = new ListNode(3);
        sol.deleteNode(mid);
        assert arrayEquals(toArray(h2), new int[]{1, 3}) : "should be [1,3]";

        System.out.println("All test cases passed ✅");
    }
}
