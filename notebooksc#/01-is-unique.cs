using System;
using System.Collections.Generic;
using System.Diagnostics;

public class Solution01IsUnique
{
    // Solution 1: Using HashSet - O(n) time, O(n) space
    public bool IsUniqueSet(string astr)
    {
        HashSet<char> seen = new HashSet<char>();
        foreach (char c in astr)
        {
            if (!seen.Add(c))
                return false;
        }
        return true;
    }

    // Solution 2: Using bit mask - O(n) time, O(1) space (for lowercase a-z only)
    public bool IsUniqueBit(string astr)
    {
        int mark = 0;
        foreach (char c in astr)
        {
            int moveBit = c - 'a';
            if ((mark & (1 << moveBit)) != 0)
                return false;
            mark |= (1 << moveBit);
        }
        return true;
    }

    static void Main()
    {
        var sol = new Solution01IsUnique();

        // Test IsUniqueSet
        Debug.Assert(sol.IsUniqueSet("abc") == true);
        Debug.Assert(sol.IsUniqueSet("leetcode") == false);
        Debug.Assert(sol.IsUniqueSet("algorithm") == true);
        Debug.Assert(sol.IsUniqueSet("hello") == false);
        Debug.Assert(sol.IsUniqueSet("") == true);

        // Test IsUniqueBit
        Debug.Assert(sol.IsUniqueBit("abc") == true);
        Debug.Assert(sol.IsUniqueBit("leetcode") == false);
        Debug.Assert(sol.IsUniqueBit("algorithm") == true);
        Debug.Assert(sol.IsUniqueBit("hello") == false);
        Debug.Assert(sol.IsUniqueBit("") == true);

        Console.WriteLine("All test cases passed ✅");
    }
}
