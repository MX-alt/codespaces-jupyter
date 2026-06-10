#include <cassert>
#include <iostream>

using namespace std;

int add(int a, int b) {
    while (b != 0) {
        unsigned int carry = static_cast<unsigned int>(a & b) << 1;
        a = a ^ b;
        b = static_cast<int>(carry);
    }
    return a;
}

int main() {
    assert(add(1, 2) == 3);
    assert(add(5, 0) == 5);
    assert(add(-1, 1) == 0);
    assert(add(-3, -4) == -7);
    assert(add(123, 456) == 579);
    assert(add(0x7fffffff, 1) == static_cast<int>(0x80000000u));

    cout << "All test cases passed ✅" << endl;
    return 0;
}
