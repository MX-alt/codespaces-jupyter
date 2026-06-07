from helpers import load_py


mod = load_py("13-balanced_binary_tree.py", "balanced_binary_tree")


def test_is_balanced_empty_tree():
    assert mod.Solution().isBalanced(None) is True


def test_is_balanced_single_node():
    assert mod.Solution().isBalanced(mod.build_tree([1])) is True


def test_is_balanced_standard_balanced_tree():
    root = mod.build_tree([3, 9, 20, None, None, 15, 7])

    assert mod.Solution().isBalanced(root) is True


def test_is_balanced_unbalanced_tree():
    root = mod.build_tree([1, 2, 2, 3, 3, None, None, 4, 4])

    assert mod.Solution().isBalanced(root) is False


def test_is_balanced_right_skewed_tree():
    root = mod.TreeNode(1, None, mod.TreeNode(2, None, mod.TreeNode(3)))

    assert mod.Solution().isBalanced(root) is False
