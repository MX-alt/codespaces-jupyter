#include <iostream>
#include <string>
#include <unordered_set>
#include <cassert>

using namespace std;

// Solution 1: Using unordered_set - O(n) time, O(n) space
bool isUniqueSet(const string& astr) {
    unordered_set<char> seen;
    for (char c : astr) {
        if (seen.count(c) > 0) {
            return false;
        }
        seen.insert(c);
    }
    return true;
}

// Solution 2: Using bit mask - O(n) time, O(1) space (for lowercase a-z only)
bool isUniqueBit(const string& astr) {
    int mark = 0;
    for (char c : astr) {
        int move_bit = c - 'a';
        if ((mark & (1 << move_bit)) != 0) {
            return false;
        }
        mark |= (1 << move_bit);
    }
    return true;
}

int main() {
    // Test isUniqueSet
    assert(isUniqueSet("abc") == true);
    assert(isUniqueSet("leetcode") == false);
    assert(isUniqueSet("algorithm") == true);
    assert(isUniqueSet("hello") == false);
    assert(isUniqueSet("") == true);

    // Test isUniqueBit
    assert(isUniqueBit("abc") == true);
    assert(isUniqueBit("leetcode") == false);
    assert(isUniqueBit("algorithm") == true);
    assert(isUniqueBit("hello") == false);
    assert(isUniqueBit("") == true);

    cout << "All test cases passed ✅" << endl;
    return 0;
}
