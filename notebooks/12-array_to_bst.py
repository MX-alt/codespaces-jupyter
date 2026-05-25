from __future__ import annotations


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        if not nums:
            return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left  = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])
        return node


def is_valid_bst(node: TreeNode | None, lo: float = float('-inf'), hi: float = float('inf')) -> bool:
    if node is None:
        return True
    if not (lo < node.val < hi):
        return False
    return is_valid_bst(node.left, lo, node.val) and is_valid_bst(node.right, node.val, hi)


def height(node: TreeNode | None) -> int:
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


def is_height_balanced(node: TreeNode | None) -> bool:
    if node is None:
        return True
    return (abs(height(node.left) - height(node.right)) <= 1
            and is_height_balanced(node.left)
            and is_height_balanced(node.right))


def inorder(node: TreeNode | None) -> list[int]:
    if node is None:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)


if __name__ == "__main__":
    s = Solution()

    # 用例 1: 空数组 → None
    assert s.sortedArrayToBST([]) is None

    # 用例 2: 单元素
    t = s.sortedArrayToBST([1])
    assert t.val == 1 and t.left is None and t.right is None

    # 用例 3: 奇数长度 [-10, -3, 0, 5, 9]
    t = s.sortedArrayToBST([-10, -3, 0, 5, 9])
    assert inorder(t) == [-10, -3, 0, 5, 9]
    assert is_valid_bst(t)
    assert is_height_balanced(t)

    # 用例 4: 偶数长度 [1, 2, 3, 4]
    t = s.sortedArrayToBST([1, 2, 3, 4])
    assert inorder(t) == [1, 2, 3, 4]
    assert is_valid_bst(t)
    assert is_height_balanced(t)

    # 用例 5: 较长数组，验证高度平衡
    t = s.sortedArrayToBST(list(range(1, 16)))
    assert inorder(t) == list(range(1, 16))
    assert is_valid_bst(t)
    assert is_height_balanced(t)

    print("所有测试用例通过 ✅")
