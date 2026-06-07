#include <iostream>
#include <string>
#include <cassert>

using namespace std;

// Solution 1: Using two-pointer approach from back - O(n) time, O(1) extra space
string replaceSpaces(string chars, int trueLength) {
    int spaceCount = 0;
    for (int i = 0; i < trueLength; i++) {
        if (chars[i] == ' ') {
            spaceCount++;
        }
    }
    
    int newIndex = trueLength + spaceCount * 2;
    
    for (int i = trueLength - 1; i >= 0; i--) {
        if (chars[i] == ' ') {
            chars[newIndex - 1] = '0';
            chars[newIndex - 2] = '2';
            chars[newIndex - 3] = '%';
            newIndex -= 3;
        } else {
            chars[newIndex - 1] = chars[i];
            newIndex--;
        }
    }
    
    // Remove trailing spaces
    while (!chars.empty() && chars.back() == ' ') {
        chars.pop_back();
    }
    
    return chars;
}

// Solution 2: Using simple string replacement
string replaceSpacesPythonic(const string& s, int trueLength) {
    string result = s.substr(0, trueLength);
    string replaced = "";
    
    for (char c : result) {
        if (c == ' ') {
            replaced += "%20";
        } else {
            replaced += c;
        }
    }
    
    return replaced;
}

int main() {
    // Test replaceSpaces
    assert(replaceSpaces("Mr John Smith    ", 13) == "Mr%20John%20Smith");
    assert(replaceSpaces("a b  ", 3) == "a%20b");
    assert(replaceSpaces("abc", 3) == "abc");
    
    // Test replaceSpacesPythonic
    assert(replaceSpacesPythonic("Mr John Smith    ", 13) == "Mr%20John%20Smith");
    assert(replaceSpacesPythonic("a b  ", 3) == "a%20b");
    assert(replaceSpacesPythonic("abc", 3) == "abc");
    
    cout << "All test cases passed ✅" << endl;
    return 0;
}
