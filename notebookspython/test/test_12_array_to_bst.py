from helpers import load_py


mod = load_py("12-array_to_bst.py", "array_to_bst")


def test_sorted_array_to_bst_empty_array():
    assert mod.Solution().sortedArrayToBST([]) is None


def test_sorted_array_to_bst_single_element():
    tree = mod.Solution().sortedArrayToBST([1])

    assert tree.val == 1
    assert tree.left is None
    assert tree.right is None


def test_sorted_array_to_bst_preserves_order_and_balance():
    nums = [-10, -3, 0, 5, 9]

    tree = mod.Solution().sortedArrayToBST(nums)

    assert mod.inorder(tree) == nums
    assert mod.is_valid_bst(tree)
    assert mod.is_height_balanced(tree)


def test_sorted_array_to_bst_even_length_array():
    nums = [1, 2, 3, 4]

    tree = mod.Solution().sortedArrayToBST(nums)

    assert mod.inorder(tree) == nums
    assert mod.is_valid_bst(tree)
    assert mod.is_height_balanced(tree)
