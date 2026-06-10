#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>

using namespace std;

int reverseBits(int num) {
    if (num == -1) return 32;

    int current = 0;
    int flipped = 0;
    int maxLen = 0;
    uint32_t u = static_cast<uint32_t>(num);

    for (int i = 0; i < 32; i++) {
        if ((u & 1u) == 1u) {
            current++;
            flipped++;
        } else {
            flipped = current + 1;
            current = 0;
        }
        maxLen = max(maxLen, flipped);
        u >>= 1;
    }

    return maxLen;
}

int main() {
    cout << "🚦 开始执行位运算算法硬核全测..." << endl;
    assert(reverseBits(1775) == 8);
    assert(reverseBits(7) == 4);
    assert(reverseBits(-1) == 32);
    assert(reverseBits(-2) == 32);
    assert(reverseBits(-3) == 32);
    assert(reverseBits(0) == 1);

    cout << "✅ 恭喜，所有断言物理通关！代码质量稳如磐石。" << endl;
    return 0;
}
