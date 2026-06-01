import java.util.ArrayDeque;
import java.util.Queue;

public class _13BalancedBinaryTree {

    static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int val) { this.val = val; }
    }

    // 後序遍历：-1 は失衡を表す。失衡が検出された時点で即座に上位へ伝播する
    public boolean isBalanced(TreeNode root) {
        return check(root) != -1;
    }

    private int check(TreeNode node) {
        if (node == null) return 0;
        int left = check(node.left);
        if (left == -1) return -1;
        int right = check(node.right);
        if (right == -1) return -1;
        if (Math.abs(left - right) > 1) return -1;
        return 1 + Math.max(left, right);
    }

    // ── 補助関数：層序配列から二分木を構築 ──────────────────────

    static TreeNode buildTree(Integer... vals) {
        if (vals.length == 0 || vals[0] == null) return null;
        TreeNode root = new TreeNode(vals[0]);
        Queue<TreeNode> queue = new ArrayDeque<>();
        queue.add(root);
        int i = 1;
        while (!queue.isEmpty() && i < vals.length) {
            TreeNode node = queue.poll();
            if (i < vals.length && vals[i] != null) {
                node.left = new TreeNode(vals[i]);
                queue.add(node.left);
            }
            i++;
            if (i < vals.length && vals[i] != null) {
                node.right = new TreeNode(vals[i]);
                queue.add(node.right);
            }
            i++;
        }
        return root;
    }

    public static void main(String[] args) {
        _13BalancedBinaryTree sol = new _13BalancedBinaryTree();

        // 空树 → true
        assert sol.isBalanced(null) == true;

        // 単一ノード → true
        assert sol.isBalanced(buildTree(1)) == true;

        // 標準的な平衡木 [3,9,20,null,null,15,7] → true
        assert sol.isBalanced(buildTree(3, 9, 20, null, null, 15, 7)) == true;

        // 失衡木 [1,2,2,3,3,null,null,4,4] → false
        assert sol.isBalanced(buildTree(1, 2, 2, 3, 3, null, null, 4, 4)) == false;

        // 右偏チェーン（退化リスト）→ false
        TreeNode skewed = new TreeNode(1);
        skewed.right = new TreeNode(2);
        skewed.right.right = new TreeNode(3);
        assert sol.isBalanced(skewed) == false;

        System.out.println("All test cases passed ✅");
    }
}
