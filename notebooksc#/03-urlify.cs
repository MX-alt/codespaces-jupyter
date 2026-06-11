using System;
using System.Diagnostics;

public class Solution03URLify
{
    // Solution 1: In-place replacement with proper space allocation
    public string ReplaceSpaces(string chars, int trueLength)
    {
        char[] charArray = chars.ToCharArray();
        int spaceCount = 0;

        // Count spaces in the true string section
        for (int i = 0; i < trueLength; i++)
        {
            if (charArray[i] == ' ')
                spaceCount++;
        }

        int newIndex = trueLength + spaceCount * 2;

        // Replace spaces from right to left
        for (int i = trueLength - 1; i >= 0; i--)
        {
            if (charArray[i] == ' ')
            {
                charArray[newIndex - 1] = '0';
                charArray[newIndex - 2] = '2';
                charArray[newIndex - 3] = '%';
                newIndex -= 3;
            }
            else
            {
                charArray[newIndex - 1] = charArray[i];
                newIndex--;
            }
        }

        return new string(charArray, 0, trueLength + spaceCount * 2);
    }

    // Solution 2: Simple approach using built-in Replace
    public string URLifySimple(string s, int trueLength)
    {
        return s.Substring(0, trueLength).Replace(" ", "%20");
    }

    static void Main()
    {
        var sol = new Solution03URLify();

        Debug.Assert(sol.ReplaceSpaces("Mr John Smith    ", 13) == "Mr%20John%20Smith");
        Debug.Assert(sol.ReplaceSpaces("a b  ", 3) == "a%20b");
        Debug.Assert(sol.ReplaceSpaces("abc", 3) == "abc");
        Debug.Assert(sol.URLifySimple("Mr John Smith    ", 13) == "Mr%20John%20Smith");

        Console.WriteLine("All test cases passed ✅");
    }
}
