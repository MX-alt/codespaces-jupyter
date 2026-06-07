#include <iostream>
#include <string>
#include <algorithm>
#include <cassert>

using namespace std;

// Solution 1: Using sort - O(n log n) time, O(n) space
bool isAnagramSort(string s1, string s2) {
    if (s1.length() != s2.length()) {
        return false;
    }
    
    sort(s1.begin(), s1.end());
    sort(s2.begin(), s2.end());
    
    return s1 == s2;
}

// Solution 2: Using character count array - O(n) time, O(1) space (for lowercase a-z only)
bool checkPermutation(const string& s1, const string& s2) {
    if (s1.length() != s2.length()) {
        return false;
    }
    
    int counts[26] = {0};
    
    for (char c : s1) {
        counts[c - 'a']++;
    }
    
    for (char c : s2) {
        counts[c - 'a']--;
    }
    
    for (int i = 0; i < 26; i++) {
        if (counts[i] != 0) {
            return false;
        }
    }
    
    return true;
}

int main() {
    // Test isAnagramSort
    assert(isAnagramSort("abc", "cba") == true);
    assert(isAnagramSort("apple", "pale") == false);
    assert(isAnagramSort("listen", "silent") == true);
    assert(isAnagramSort("hello", "world") == false);
    
    // Test checkPermutation
    assert(checkPermutation("abc", "cba") == true);
    assert(checkPermutation("apple", "pale") == false);
    assert(checkPermutation("listen", "silent") == true);
    assert(checkPermutation("hello", "world") == false);
    
    cout << "All test cases passed ✅" << endl;
    return 0;
}
