using System;
using System.Collections.Generic;
using System.Diagnostics;

public class Solution08TripleInOne
{
    private readonly int stackSize;
    private readonly int[] array;
    private readonly int[] sizes;

    public Solution08TripleInOne(int stackSize)
    {
        this.stackSize = stackSize;
        this.array = new int[stackSize * 3];
        this.sizes = new int[3];
    }

    public void Push(int stackNum, int value)
    {
        if (sizes[stackNum] == stackSize)
        {
            Console.WriteLine($"❌ Stack {stackNum} is full, cannot push {value}");
            return;
        }
        int absIndex = stackNum * stackSize + sizes[stackNum];
        array[absIndex] = value;
        sizes[stackNum]++;
    }

    public int Pop(int stackNum)
    {
        if (sizes[stackNum] == 0)
        {
            Console.WriteLine($"⚠️ Stack {stackNum} is empty, cannot pop");
            return -1;
        }
        sizes[stackNum]--;
        int absIndex = stackNum * stackSize + sizes[stackNum];
        return array[absIndex];
    }

    public int Peek(int stackNum)
    {
        if (sizes[stackNum] == 0)
        {
            Console.WriteLine($"👀 Stack {stackNum} is empty");
            return -1;
        }
        int absIndex = stackNum * stackSize + (sizes[stackNum] - 1);
        return array[absIndex];
    }

    public bool IsEmpty(int stackNum)
    {
        return sizes[stackNum] == 0;
    }

    static void Main()
    {
        var obj = new Solution08TripleInOne(2);

        // Test case 1: Basic push/peek/pop
        obj.Push(0, 10);
        obj.Push(0, 20);
        Debug.Assert(obj.Peek(0) == 20, "peek should be 20");
        Debug.Assert(obj.Pop(0) == 20, "pop should return 20");
        Debug.Assert(obj.Peek(0) == 10, "peek should be 10 after pop");
        Debug.Assert(!obj.IsEmpty(0), "stack 0 should not be empty");
        obj.Pop(0);
        Debug.Assert(obj.IsEmpty(0), "stack 0 should be empty");

        // Test case 2: Push when full is ignored
        obj.Push(1, 1);
        obj.Push(1, 2);
        obj.Push(1, 3); // ignored, stack is full
        Debug.Assert(obj.Peek(1) == 2, "stack 1 top should still be 2");

        // Test case 3: Pop from empty stack
        Debug.Assert(obj.Pop(2) == -1, "pop from empty stack should return -1");

        // Test case 4: Each stack is independent
        obj.Push(2, 99);
        Debug.Assert(obj.Peek(2) == 99, "stack 2 should have 99");
        Debug.Assert(obj.Peek(1) == 2, "stack 1 should be unaffected");

        Console.WriteLine("All test cases passed ✅");
    }
}
