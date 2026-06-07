#include <iostream>
#include <string>
#include <unordered_set>
#include <cctype>
#include <cassert>

using namespace std;

// Using set cancellation method: if at most 1 character appears an odd number of times,
// the string can be rearranged to form a palindrome
bool canPermutePalindrome(string s) {
    // Remove spaces and convert to lowercase
    string cleaned = "";
    for (char c : s) {
        if (c != ' ') {
            cleaned += tolower(c);
        }
    }
    
    unordered_set<char> oddChars;
    
    for (char c : cleaned) {
        if (oddChars.count(c) > 0) {
            oddChars.erase(c);
        } else {
            oddChars.insert(c);
        }
    }
    
    return oddChars.size() <= 1;
}

int main() {
    assert(canPermutePalindrome("code") == false);
    assert(canPermutePalindrome("tactcoa") == true);
    assert(canPermutePalindrome("aab") == true);
    assert(canPermutePalindrome("a") == true);
    assert(canPermutePalindrome("") == true);
    assert(canPermutePalindrome("Tact Coa") == true);
    
    cout << "All test cases passed ✅" << endl;
    return 0;
}
