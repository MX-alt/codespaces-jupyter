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

public class Solution10Intersection
{
    // Find intersection node using HashSet
    public ListNode GetIntersectionNodeSet(ListNode headA, ListNode headB)
    {
        if (headA == null || headB == null)
            return null;

        HashSet<ListNode> seen = new HashSet<ListNode>();

        while (headA != null)
        {
            seen.Add(headA);
            headA = headA.Next;
        }

        while (headB != null)
        {
            if (seen.Contains(headB))
                return headB;
            headB = headB.Next;
        }

        return null;
    }

    // Find intersection node using two pointers
    // The two pointers will meet at intersection node if it exists
    public ListNode GetIntersectionNode(ListNode headA, ListNode headB)
    {
        if (headA == null || headB == null)
            return null;

        ListNode a = headA;
        ListNode b = headB;

        while (a != b)
        {
            a = (a == null) ? headB : a.Next;
            b = (b == null) ? headA : b.Next;
        }

        return a;
    }

    // Helper function to build a shared tail
    public ListNode BuildSharedTail(params int[] vals)
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

    // Helper function to build a prefix and attach to tail
    public ListNode BuildPrefix(ListNode tail, params int[] vals)
    {
        if (vals.Length == 0)
            return tail;

        ListNode head = new ListNode(vals[0]);
        ListNode curr = head;

        for (int i = 1; i < vals.Length; i++)
        {
            curr.Next = new ListNode(vals[i]);
            curr = curr.Next;
        }

        curr.Next = tail;
        return head;
    }

    // Helper function to delete list (up to stop node)
    public void DeleteList(ListNode head, ListNode stop = null)
    {
        while (head != null && head != stop)
        {
            ListNode temp = head;
            head = head.Next;
        }
    }

    static void Main()
    {
        var sol = new Solution10Intersection();

        // Test case 1: No intersection
        ListNode headA1 = sol.BuildPrefix(null, 1, 9, 1, 2);
        ListNode headB1 = sol.BuildPrefix(null, 3);
        Debug.Assert(sol.GetIntersectionNode(headA1, headB1) == null, "No intersection expected");
        Debug.Assert(sol.GetIntersectionNodeSet(headA1, headB1) == null, "No intersection expected (set)");

        // Test case 2: Intersection at beginning of second list
        ListNode shared2 = sol.BuildSharedTail(2, 4);
        ListNode headA2 = sol.BuildPrefix(shared2, 3);
        ListNode headB2 = shared2;
        ListNode intersection2 = sol.GetIntersectionNode(headA2, headB2);
        Debug.Assert(intersection2 != null && intersection2.Val == 2, "Intersection should be 2");
        Debug.Assert(sol.GetIntersectionNodeSet(headA2, headB2).Val == 2, "Intersection should be 2 (set)");

        // Test case 3: Intersection in the middle
        ListNode shared3 = sol.BuildSharedTail(8, 4, 5);
        ListNode headA3 = sol.BuildPrefix(shared3, 4, 1);
        ListNode headB3 = sol.BuildPrefix(shared3, 5, 6, 1);
        ListNode intersection3 = sol.GetIntersectionNode(headA3, headB3);
        Debug.Assert(intersection3 != null && intersection3.Val == 8, "Intersection should be 8");
        Debug.Assert(sol.GetIntersectionNodeSet(headA3, headB3).Val == 8, "Intersection should be 8 (set)");

        // Test case 4: Both null
        Debug.Assert(sol.GetIntersectionNode(null, null) == null, "Both null → null");
        Debug.Assert(sol.GetIntersectionNodeSet(null, null) == null, "Both null → null (set)");

        Console.WriteLine("All test cases passed ✅");
    }
}
