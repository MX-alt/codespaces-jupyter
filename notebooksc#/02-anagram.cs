using System;
using System.Diagnostics;

public class Solution02Anagram
{
    // Solution 1: Using sorting
    public bool IsAnagramSort(string s1, string s2)
    {
        if (s1.Length != s2.Length)
            return false;

        char[] arr1 = s1.ToCharArray();
        char[] arr2 = s2.ToCharArray();
        Array.Sort(arr1);
        Array.Sort(arr2);

        return new string(arr1) == new string(arr2);
    }

    // Solution 2: Using character count array
    public bool CheckPermutation(string s1, string s2)
    {
        if (s1.Length != s2.Length)
            return false;

        int[] counts = new int[26];

        foreach (char c in s1)
        {
            int index = c - 'a';
            counts[index]++;
        }

        foreach (char c in s2)
        {
            int index = c - 'a';
            counts[index]--;
        }

        foreach (int count in counts)
        {
            if (count != 0)
                return false;
        }

        return true;
    }

    static void Main()
    {
        var sol = new Solution02Anagram();

        Debug.Assert(sol.IsAnagramSort("abc", "cba") == true);
        Debug.Assert(sol.IsAnagramSort("apple", "pale") == false);
        Debug.Assert(sol.CheckPermutation("abc", "cba") == true);
        Debug.Assert(sol.CheckPermutation("apple", "pale") == false);

        Console.WriteLine("All test cases passed ✅");
    }
}
