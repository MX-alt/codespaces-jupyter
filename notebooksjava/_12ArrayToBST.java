import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

public class _12ArrayToBST {

    static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int val) { this.val = val; }
    }

    // 中央要素をルートにして再帰的に左右サブツリーを構築する
    public TreeNode sortedArrayToBST(int[] nums) {
        return build(nums, 0, nums.length - 1);
    }

    private TreeNode build(int[] nums, int lo, int hi) {
        if (lo > hi) return null;
        int mid = (lo + hi) / 2;
        TreeNode node = new TreeNode(nums[mid]);
        node.left  = build(nums, lo, mid - 1);
        node.right = build(nums, mid + 1, hi);
        return node;
    }

    // ── 検証ユーティリティ ────────────────────────────────────

    static boolean isValidBST(TreeNode node, long lo, long hi) {
        if (node == null) return true;
        if (node.val <= lo || node.val >= hi) return false;
        return isValidBST(node.left, lo, node.val) && isValidBST(node.right, node.val, hi);
    }

    static int height(TreeNode node) {
        if (node == null) return 0;
        return 1 + Math.max(height(node.left), height(node.right));
    }

    static boolean isHeightBalanced(TreeNode node) {
        if (node == null) return true;
        return Math.abs(height(node.left) - height(node.right)) <= 1
                && isHeightBalanced(node.left)
                && isHeightBalanced(node.right);
    }

    static List<Integer> inorder(TreeNode node) {
        List<Integer> result = new ArrayList<>();
        inorderHelper(node, result);
        return result;
    }

    static void inorderHelper(TreeNode node, List<Integer> result) {
        if (node == null) return;
        inorderHelper(node.left, result);
        result.add(node.val);
        inorderHelper(node.right, result);
    }

    public static void main(String[] args) {
        _12ArrayToBST sol = new _12ArrayToBST();

        // 空配列 → null
        assert sol.sortedArrayToBST(new int[]{}) == null;

        // 単一要素
        TreeNode t = sol.sortedArrayToBST(new int[]{1});
        assert t.val == 1 && t.left == null && t.right == null;

        // 奇数長 [-10,-3,0,5,9]
        t = sol.sortedArrayToBST(new int[]{-10, -3, 0, 5, 9});
        assert inorder(t).equals(List.of(-10, -3, 0, 5, 9));
        assert isValidBST(t, Long.MIN_VALUE, Long.MAX_VALUE);
        assert isHeightBalanced(t);

        // 偶数長 [1,2,3,4]
        t = sol.sortedArrayToBST(new int[]{1, 2, 3, 4});
        assert inorder(t).equals(List.of(1, 2, 3, 4));
        assert isValidBST(t, Long.MIN_VALUE, Long.MAX_VALUE);
        assert isHeightBalanced(t);

        // 長い配列（1〜15）
        int[] nums = new int[15];
        for (int i = 0; i < 15; i++) nums[i] = i + 1;
        t = sol.sortedArrayToBST(nums);
        List<Integer> expected = new ArrayList<>();
        for (int i = 1; i <= 15; i++) expected.add(i);
        assert inorder(t).equals(expected);
        assert isValidBST(t, Long.MIN_VALUE, Long.MAX_VALUE);
        assert isHeightBalanced(t);

        System.out.println("All test cases passed ✅");
    }
}
