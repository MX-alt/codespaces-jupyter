#include <cassert>
#include <iostream>

using namespace std;

int waysToClimb(int n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;
    if (n == 2) return 2;
    if (n == 3) return 4;

    int a = 1, b = 2, c = 4;
    for (int i = 0; i < n - 3; i++) {
        int next = a + b + c;
        a = b;
        b = c;
        c = next;
    }
    return c;
}

int main() {
    assert(waysToClimb(0) == 0);
    assert(waysToClimb(-1) == 0);
    assert(waysToClimb(1) == 1);
    assert(waysToClimb(2) == 2);
    assert(waysToClimb(3) == 4);
    assert(waysToClimb(4) == 7);
    assert(waysToClimb(5) == 13);
    assert(waysToClimb(10) == 274);

    cout << "All test cases passed ✅" << endl;
    return 0;
}
