from __future__ import annotations


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        """后序遍历，返回 -1 表示子树已失衡，否则返回实际高度。
        一旦发现失衡立即向上传播，避免重复计算高度。
        """
        def check(node: TreeNode | None) -> int:
            if node is None:
                return 0
            left = check(node.left)
            if left == -1:
                return -1
            right = check(node.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1


# ── 辅助：用列表构造完全二叉树（None 表示空节点，层序排列）──────

def build_tree(vals: list[int | None]) -> TreeNode | None:
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    queue = [root]
    i = 1
    while queue and i < len(vals):
        node = queue.pop(0)
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    s = Solution()

    # 用例 1: 空树 → True
    assert s.isBalanced(None) is True

    # 用例 2: 单节点 → True
    assert s.isBalanced(build_tree([1])) is True

    # 用例 3: 标准平衡树 [3,9,20,None,None,15,7] → True
    #        3
    #       / \
    #      9  20
    #         / \
    #        15   7
    assert s.isBalanced(build_tree([3, 9, 20, None, None, 15, 7])) is True

    # 用例 4: 失衡树 [1,2,2,3,3,None,None,4,4] → False
    #            1
    #           / \
    #          2   2
    #         / \
    #        3   3
    #       / \
    #      4   4
    assert s.isBalanced(build_tree([1, 2, 2, 3, 3, None, None, 4, 4])) is False

    # 用例 5: 右偏链状树（退化为链表）→ False
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert s.isBalanced(root) is False

    print("所有测试用例通过 ✅")
