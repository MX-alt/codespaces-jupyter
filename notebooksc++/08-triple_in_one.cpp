#include <iostream>
#include <array>
#include <string>
#include <cassert>

using namespace std;

class TripleInOne {
public:
    TripleInOne(int stackSize) : stackSize(stackSize), array(stackSize * 3), sizes{0, 0, 0} {}

    string push(int stackNum, int value) {
        if (sizes[stackNum] == stackSize) {
            return "❌ 【错误】stack " + to_string(stackNum) + " 已满，无法 push " + to_string(value);
        }
        int index = stackNum * stackSize + sizes[stackNum];
        array[index] = value;
        sizes[stackNum]++;
        return "📥 【Push成功】stack " + to_string(stackNum) + " push " + to_string(value);
    }

    string pop(int stackNum) {
        if (sizes[stackNum] == 0) {
            return "⚠️ 【警告】stack " + to_string(stackNum) + " 已空，无法 pop";
        }
        sizes[stackNum]--;
        int index = stackNum * stackSize + sizes[stackNum];
        int value = array[index];
        return "📤 【Pop成功】stack " + to_string(stackNum) + " pop " + to_string(value);
    }

    string peek(int stackNum) {
        if (sizes[stackNum] == 0) {
            return "👀 【Peek】stack " + to_string(stackNum) + " 为空";
        }
        int index = stackNum * stackSize + sizes[stackNum] - 1;
        return "👀 【Peek】stack " + to_string(stackNum) + " top " + to_string(array[index]);
    }

    string isEmpty(int stackNum) {
        if (sizes[stackNum] == 0) {
            return "❓ 【状态】stack " + to_string(stackNum) + " 为空";
        }
        return "❓ 【状态】stack " + to_string(stackNum) + " 大小 " + to_string(sizes[stackNum]);
    }

private:
    int stackSize;
    vector<int> array;
    array<int, 3> sizes;
};

int main() {
    TripleInOne obj(1);

    string result1 = obj.push(0, 1);
    assert(result1.find("Push") != string::npos);

    string result2 = obj.push(0, 2);
    assert(result2.find("已满") != string::npos);

    string result3 = obj.pop(0);
    assert(result3.find("Pop成功") != string::npos);

    string result4 = obj.pop(0);
    assert(result4.find("已空") != string::npos);

    string result5 = obj.pop(0);
    assert(result5.find("已空") != string::npos);

    string result6 = obj.isEmpty(0);
    assert(result6.find("为空") != string::npos);

    cout << "All test cases passed ✅" << endl;
    return 0;
}
