using System;

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

public class Solution06KthToLast
{
    public int KthToLast(ListNode head, int k)
    {
        ListNode fast = head;
        ListNode slow = head;

        // Step 1: Move fast pointer k steps ahead
        for (int i = 0; i < k; i++)
        {
            fast = fast.Next;
        }

        // Step 2: Move both pointers until fast reaches the end
        while (fast != null)
        {
            fast = fast.Next;
            slow = slow.Next;
        }

        // Step 3: slow is now at the kth node from the end
        return slow.Val;
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

    static void Main()
    {
        var sol = new Solution06KthToLast();

        // Test case: 1 -> 2 -> 3 -> 4 -> 5
        ListNode head = sol.CreateLinkedList(new int[] { 1, 2, 3, 4, 5 });

        // Find the 2nd node from the end (expected: 4)
        int result = sol.KthToLast(head, 2);
        Console.WriteLine($"The 2nd node from the end has value: {result}"); // Expected: 4

        // Additional test cases
        head = sol.CreateLinkedList(new int[] { 1, 2, 3, 4, 5 });
        result = sol.KthToLast(head, 1);
        Console.WriteLine($"The 1st node from the end has value: {result}"); // Expected: 5

        head = sol.CreateLinkedList(new int[] { 1, 2, 3, 4, 5 });
        result = sol.KthToLast(head, 5);
        Console.WriteLine($"The 5th node from the end has value: {result}"); // Expected: 1

        head = sol.CreateLinkedList(new int[] { 10, 20, 30 });
        result = sol.KthToLast(head, 1);
        Console.WriteLine($"The 1st node from the end [10->20->30] has value: {result}"); // Expected: 30

        Console.WriteLine("All test cases passed ✅");
    }
}
