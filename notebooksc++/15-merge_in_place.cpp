#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

void merge(vector<int>& nums1, int m, const vector<int>& nums2, int n) {
    int i = m - 1;
    int j = n - 1;
    int k = m + n - 1;

    while (i >= 0 && j >= 0) {
        if (nums1[i] >= nums2[j]) {
            nums1[k--] = nums1[i--];
        } else {
            nums1[k--] = nums2[j--];
        }
    }

    while (j >= 0) {
        nums1[k--] = nums2[j--];
    }
}

int main() {
    vector<int> a = {1, 3, 5, 0, 0, 0};
    merge(a, 3, {2, 4, 6}, 3);
    assert(a == vector<int>({1, 2, 3, 4, 5, 6}));

    a = {1, 2, 3};
    merge(a, 3, {}, 0);
    assert(a == vector<int>({1, 2, 3}));

    a = {0, 0, 0};
    merge(a, 0, {1, 2, 3}, 3);
    assert(a == vector<int>({1, 2, 3}));

    a = {4, 5, 6, 0, 0, 0};
    merge(a, 3, {1, 2, 3}, 3);
    assert(a == vector<int>({1, 2, 3, 4, 5, 6}));

    a = {1, 2, 2, 0, 0};
    merge(a, 3, {2, 3}, 2);
    assert(a == vector<int>({1, 2, 2, 2, 3}));

    a = {2, 0};
    merge(a, 1, {1}, 1);
    assert(a == vector<int>({1, 2}));

    cout << "All test cases passed ✅" << endl;
    return 0;
}
