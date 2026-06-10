#include <cassert>
#include <iostream>

using namespace std;

int trailingZeroes(int n) {
    int count = 0;
    while (n > 0) {
        n /= 5;
        count += n;
    }
    return count;
}

int main() {
    assert(trailingZeroes(3) == 0);
    assert(trailingZeroes(5) == 1);
    assert(trailingZeroes(10) == 2);
    assert(trailingZeroes(25) == 6);
    assert(trailingZeroes(125) == 31);
    assert(trailingZeroes(0) == 0);

    cout << "All test cases passed ✅" << endl;
    return 0;
}
