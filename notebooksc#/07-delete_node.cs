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

public class Solution07DeleteNode
{
    // Delete node in-place by copying next node's value and skipping it
    public void DeleteNode(ListNode node)
    {
        if (node == null || node.Next == null)
        {
            return;
        }
        node.Val = node.Next.Val;
        node.Next = node.Next.Next;
    }

    // Helper function to create a linked list from an array
    public ListNode CreateLinkedList(int[] values)
    {
        if (values.Length == 0)
            return null;

        ListNode head = new ListNode(values[0]);
        ListNode current = head;

        for (int i = 1; i < values.Length; i++)
        {
            current.Next = new ListNode(values[i]);
            current = current.Next;
        }

        return head;
    }

    // Helper function to convert linked list to array
    public List<int> LinkedListToList(ListNode head)
    {
        List<int> result = new List<int>();
        while (head != null)
        {
            result.Add(head.Val);
            head = head.Next;
        }
        return result;
    }

    // Helper function to compare two lists
    public bool ListsEqual(List<int> list1, List<int> list2)
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
        var sol = new Solution07DeleteNode();

        // Test case 1: Delete node 5 from 4 -> 5 -> 1 -> 9
        ListNode head1 = sol.CreateLinkedList(new int[] { 4, 5, 1, 9 });
        ListNode nodeToDelete = head1.Next;
        sol.DeleteNode(nodeToDelete);
        Debug.Assert(sol.ListsEqual(sol.LinkedListToList(head1), new List<int> { 4, 1, 9 }));

        // Test case 2: Delete node 2 from 1 -> 2 -> 3
        ListNode head2 = sol.CreateLinkedList(new int[] { 1, 2, 3 });
        ListNode mid = head2.Next;
        sol.DeleteNode(mid);
        Debug.Assert(sol.ListsEqual(sol.LinkedListToList(head2), new List<int> { 1, 3 }));

        // Test case 3: Delete single middle node from 10 -> 20 -> 30 -> 40
        ListNode head3 = sol.CreateLinkedList(new int[] { 10, 20, 30, 40 });
        ListNode nodeToDelete3 = head3.Next.Next; // node 30
        sol.DeleteNode(nodeToDelete3);
        Debug.Assert(sol.ListsEqual(sol.LinkedListToList(head3), new List<int> { 10, 20, 40 }));

        Console.WriteLine("All test cases passed ✅");
    }
}
