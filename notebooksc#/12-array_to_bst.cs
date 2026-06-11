using System;
using System.Collections.Generic;
using System.Diagnostics;

public class TreeNode
{
    public int Val { get; set; }
    public TreeNode Left { get; set; }
    public TreeNode Right { get; set; }

    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null)
    {
        Val = val;
        Left = left;
        Right = right;
    }
}

public class Solution12ArrayToBST
{
    // Build BST from sorted array using recursion
    public TreeNode SortedArrayToBST(int[] nums)
    {
        return BuildBST(nums, 0, nums.Length - 1);
    }

    private TreeNode BuildBST(int[] nums, int lo, int hi)
    {
        if (lo > hi)
            return null;

        int mid = lo + (hi - lo) / 2;
        TreeNode node = new TreeNode(nums[mid]);
        node.Left = BuildBST(nums, lo, mid - 1);
        node.Right = BuildBST(nums, mid + 1, hi);

        return node;
    }

    // Validate that tree is a valid BST
    private bool IsValidBST(TreeNode node, long lo, long hi)
    {
        if (node == null)
            return true;

        if (node.Val <= lo || node.Val >= hi)
            return false;

        return IsValidBST(node.Left, lo, node.Val) && 
               IsValidBST(node.Right, node.Val, hi);
    }

    public bool IsValidBST(TreeNode node)
    {
        return IsValidBST(node, long.MinValue, long.MaxValue);
    }

    // Calculate height of tree
    private int Height(TreeNode node)
    {
        if (node == null)
            return 0;

        return 1 + Math.Max(Height(node.Left), Height(node.Right));
    }

    // Check if tree is height balanced
    private bool IsHeightBalanced(TreeNode node)
    {
        if (node == null)
            return true;

        int leftHeight = Height(node.Left);
        int rightHeight = Height(node.Right);

        return Math.Abs(leftHeight - rightHeight) <= 1 &&
               IsHeightBalanced(node.Left) &&
               IsHeightBalanced(node.Right);
    }

    // Get inorder traversal of tree
    private List<int> Inorder(TreeNode node)
    {
        List<int> result = new List<int>();
        if (node == null)
            return result;

        result.AddRange(Inorder(node.Left));
        result.Add(node.Val);
        result.AddRange(Inorder(node.Right));

        return result;
    }

    // Helper to compare two lists
    private bool ListsEqual(List<int> list1, List<int> list2)
    {
        if (list1.Count != list2.Count)
            return false;

        for (int i = 0; i < list1.Count; i++)
        {
            if (list1[i] != list2[i])
                return false;
        }
        return true;
    }

    static void Main()
    {
        var sol = new Solution12ArrayToBST();

        // Test case 1: Empty array
        TreeNode t = sol.SortedArrayToBST(new int[] { });
        Debug.Assert(t == null, "Empty array should return null");

        // Test case 2: Single element
        t = sol.SortedArrayToBST(new int[] { 1 });
        Debug.Assert(t.Val == 1 && t.Left == null && t.Right == null, "Single element should have no children");

        // Test case 3: Odd length array
        t = sol.SortedArrayToBST(new int[] { -10, -3, 0, 5, 9 });
        List<int> expected = new List<int> { -10, -3, 0, 5, 9 };
        Debug.Assert(sol.ListsEqual(sol.Inorder(t), expected), "Inorder traversal should match input");
        Debug.Assert(sol.IsValidBST(t), "Tree should be valid BST");
        Debug.Assert(sol.IsHeightBalanced(t), "Tree should be height balanced");

        // Test case 4: Even length array
        t = sol.SortedArrayToBST(new int[] { 1, 2, 3, 4 });
        expected = new List<int> { 1, 2, 3, 4 };
        Debug.Assert(sol.ListsEqual(sol.Inorder(t), expected), "Inorder traversal should match input");
        Debug.Assert(sol.IsValidBST(t), "Tree should be valid BST");
        Debug.Assert(sol.IsHeightBalanced(t), "Tree should be height balanced");

        // Test case 5: Longer array
        t = sol.SortedArrayToBST(new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 });
        expected = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 };
        Debug.Assert(sol.ListsEqual(sol.Inorder(t), expected), "Inorder traversal should match input");
        Debug.Assert(sol.IsValidBST(t), "Tree should be valid BST");
        Debug.Assert(sol.IsHeightBalanced(t), "Tree should be height balanced");

        // Test case 6: Array with negative numbers
        t = sol.SortedArrayToBST(new int[] { -100, -50, 0, 50, 100 });
        expected = new List<int> { -100, -50, 0, 50, 100 };
        Debug.Assert(sol.ListsEqual(sol.Inorder(t), expected), "Inorder traversal should match input");
        Debug.Assert(sol.IsValidBST(t), "Tree should be valid BST");
        Debug.Assert(sol.IsHeightBalanced(t), "Tree should be height balanced");

        Console.WriteLine("All test cases passed ✅");
    }
}
