using System;
using System.Collections.Generic;
using System.Diagnostics;

public class MinStack
{
    private Stack<int> data;
    private Stack<int> minStack;

    public MinStack()
    {
        data = new Stack<int>();
        minStack = new Stack<int>();
    }

    // Push value onto stack and maintain min stack
    public void Push(int val)
    {
        data.Push(val);
        if (minStack.Count == 0 || val <= minStack.Peek())
        {
            minStack.Push(val);
        }
    }

    // Pop from stack and update min stack if needed
    public void Pop()
    {
        if (data.Count == 0)
            throw new InvalidOperationException("pop from empty stack");

        int val = data.Pop();
        if (val == minStack.Peek())
        {
            minStack.Pop();
        }
    }

    // Return top element without removing
    public int Top()
    {
        if (data.Count == 0)
            throw new InvalidOperationException("top from empty stack");

        return data.Peek();
    }

    // Return minimum element without removing
    public int Min()
    {
        if (minStack.Count == 0)
            throw new InvalidOperationException("min from empty stack");

        return minStack.Peek();
    }

    static void Main()
    {
        // Test case 1: Basic push and min
        MinStack s = new MinStack();
        s.Push(3);
        s.Push(5);
        s.Push(1);
        s.Push(2);
        Debug.Assert(s.Min() == 1, "min should be 1");
        Debug.Assert(s.Top() == 2, "top should be 2");

        // Test case 2: Min restores after pop
        s.Pop(); // Remove 2
        s.Pop(); // Remove 1 (current min)
        Debug.Assert(s.Min() == 3, "min should restore to 3");
        Debug.Assert(s.Top() == 5, "top should be 5");

        // Test case 3: Duplicate minimum values
        s.Push(3);
        s.Push(3);
        Debug.Assert(s.Min() == 3, "min should be 3");
        s.Pop();
        Debug.Assert(s.Min() == 3, "min should still be 3 after popping one duplicate");

        // Test case 4: Single element
        MinStack s2 = new MinStack();
        s2.Push(42);
        Debug.Assert(s2.Min() == 42, "min should be 42");
        Debug.Assert(s2.Top() == 42, "top should be 42");

        // Test case 5: Pop from empty stack throws exception
        MinStack s3 = new MinStack();
        bool sawPopError = false;
        try
        {
            s3.Pop();
        }
        catch (InvalidOperationException)
        {
            sawPopError = true;
        }
        Debug.Assert(sawPopError, "should throw when popping empty stack");

        // Test case 6: Multiple operations
        MinStack s4 = new MinStack();
        s4.Push(5);
        s4.Push(1);
        s4.Push(3);
        Debug.Assert(s4.Min() == 1);
        s4.Push(1);
        Debug.Assert(s4.Min() == 1);
        s4.Pop();
        Debug.Assert(s4.Min() == 1);
        s4.Pop();
        Debug.Assert(s4.Min() == 1);
        s4.Pop();
        Debug.Assert(s4.Min() == 5);

        Console.WriteLine("All test cases passed ✅");
    }
}
