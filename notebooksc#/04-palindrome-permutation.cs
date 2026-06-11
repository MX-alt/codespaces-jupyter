using System;
using System.Collections.Generic;
using System.Diagnostics;

public class Solution04PalindromePermutation
{
    // Solution: Using a set to track odd character counts
    public bool CanPermutePalindrome(string s)
    {
        s = s.Replace(" ", "").ToLower();
        
        HashSet<char> oddChars = new HashSet<char>();

        // Traverse the string and use a set to track odd counts
        foreach (char c in s)
        {
            if (oddChars.Contains(c))
                oddChars.Remove(c);
            else
                oddChars.Add(c);
        }

        // A string can be rearranged into a palindrome if at most one character has an odd count
        return oddChars.Count <= 1;
    }

    static void Main()
    {
        var sol = new Solution04PalindromePermutation();

        // Test case 1
        string test1 = "code";
        bool result1 = sol.CanPermutePalindrome(test1);
        Console.WriteLine($"'{test1}' can be rearranged to a palindrome? {result1}"); // Expected: False

        // Test case 2
        string test2 = "tactcoa";
        bool result2 = sol.CanPermutePalindrome(test2);
        Console.WriteLine($"'{test2}' can be rearranged to a palindrome? {result2}"); // Expected: True

        // Additional test cases
        Debug.Assert(sol.CanPermutePalindrome("code") == false);
        Debug.Assert(sol.CanPermutePalindrome("tactcoa") == true);
        Debug.Assert(sol.CanPermutePalindrome("a") == true);
        Debug.Assert(sol.CanPermutePalindrome("ab") == false);
        Debug.Assert(sol.CanPermutePalindrome("aab") == true);

        Console.WriteLine("All test cases passed ✅");
    }
}
