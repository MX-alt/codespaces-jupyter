using System;
using System.Collections.Generic;
using System.Diagnostics;

public class ListNode
{
    public int Val { get; set; }
    public ListNode Next { get; set; }

    public ListNode(int val = 0, ListNode next = null)
    {
        Val = val;
        Next = next;
    }
}

public class Solution09PalindromeLinkedList
{
    // Check if linked list is palindrome by collecting values in a list
    // and checking from both ends
    public bool IsPalindrome(ListNode head)
    {
        List<int> vals = new List<int>();
        ListNode curr = head;

        while (curr != null)
        {
            vals.Add(curr.Val);
            curr = curr.Next;
        }

        int left = 0;
        int right = vals.Count - 1;

        while (left < right)
        {
            if (vals[left] != vals[right])
                return false;
            left++;
            right--;
        }

        return true;
    }

    // Helper function to create a linked list from variable arguments
    public ListNode CreateList(params int[] vals)
    {
        if (vals.Length == 0)
            return null;

        ListNode head = new ListNode(vals[0]);
        ListNode curr = head;

        for (int i = 1; i < vals.Length; i++)
        {
            curr.Next = new ListNode(vals[i]);
            curr = curr.Next;
        }

        return head;
    }

    static void Main()
    {
        var sol = new Solution09PalindromeLinkedList();

        // Test case 1: null list
        Debug.Assert(sol.IsPalindrome(null) == true, "null → true");

        // Test case 2: single element
        Debug.Assert(sol.IsPalindrome(sol.CreateList(7)) == true, "[7] → true");

        // Test case 3: odd length palindrome
        Debug.Assert(sol.IsPalindrome(sol.CreateList(1, 2, 1)) == true, "[1,2,1] → true");

        // Test case 4: even length palindrome
        Debug.Assert(sol.IsPalindrome(sol.CreateList(1, 2, 2, 1)) == true, "[1,2,2,1] → true");

        // Test case 5: not a palindrome (odd length)
        Debug.Assert(sol.IsPalindrome(sol.CreateList(1, 2, 3, 1)) == false, "[1,2,3,1] → false");

        // Test case 6: not a palindrome (even length)
        Debug.Assert(sol.IsPalindrome(sol.CreateList(1, 2)) == false, "[1,2] → false");

        // Test case 7: longer palindrome
        Debug.Assert(sol.IsPalindrome(sol.CreateList(1, 2, 3, 2, 1)) == true, "[1,2,3,2,1] → true");

        Console.WriteLine("All test cases passed ✅");
    }
}
