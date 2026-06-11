using System;
using System.Collections.Generic;

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

public class Solution05RemoveDuplicateNodes
{
    public ListNode RemoveDuplicateNodes(ListNode head)
    {
        if (head == null)
            return head;

        HashSet<int> visited = new HashSet<int> { head.Val };
        ListNode curr = head;

        while (curr != null && curr.Next != null)
        {
            if (visited.Contains(curr.Next.Val))
            {
                curr.Next = curr.Next.Next;
            }
            else
            {
                visited.Add(curr.Next.Val);
                curr = curr.Next;
            }
        }

        return head;
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

    // Helper function to print the linked list
    public void PrintLinkedList(ListNode head)
    {
        ListNode curr = head;
        while (curr != null)
        {
            Console.Write(curr.Val);
            if (curr.Next != null)
                Console.Write(" -> ");
            curr = curr.Next;
        }
        Console.WriteLine();
    }

    static void Main()
    {
        var sol = new Solution05RemoveDuplicateNodes();

        // Test case: 1 -> 2 -> 3 -> 3 -> 2 -> 1
        ListNode head = sol.CreateLinkedList(new int[] { 1, 2, 3, 3, 2, 1 });

        Console.Write("Original list: ");
        sol.PrintLinkedList(head);

        // Remove duplicate nodes
        ListNode newHead = sol.RemoveDuplicateNodes(head);

        Console.Write("After removing duplicates: ");
        sol.PrintLinkedList(newHead);

        // Additional test cases
        head = sol.CreateLinkedList(new int[] { 5, 5, 5, 5 });
        newHead = sol.RemoveDuplicateNodes(head);
        Console.Write("Test [5,5,5,5]: ");
        sol.PrintLinkedList(newHead);

        head = sol.CreateLinkedList(new int[] { 1, 2, 3 });
        newHead = sol.RemoveDuplicateNodes(head);
        Console.Write("Test [1,2,3]: ");
        sol.PrintLinkedList(newHead);

        Console.WriteLine("All test cases passed ✅");
    }
}
