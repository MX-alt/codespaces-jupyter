#include <iostream>
#include <vector>
#include <stdexcept>
#include <cassert>

using namespace std;

class MinStack {
public:
    void push(int val) {
        data.push_back(val);
        if (minStack.empty() || val <= minStack.back()) {
            minStack.push_back(val);
        }
    }

    void pop() {
        if (data.empty()) {
            throw runtime_error("pop from empty stack");
        }
        int val = data.back();
        data.pop_back();
        if (val == minStack.back()) {
            minStack.pop_back();
        }
    }

    int top() const {
        if (data.empty()) {
            throw runtime_error("top from empty stack");
        }
        return data.back();
    }

    int min() const {
        if (minStack.empty()) {
            throw runtime_error("min from empty stack");
        }
        return minStack.back();
    }

private:
    vector<int> data;
    vector<int> minStack;
};

int main() {
    MinStack s;
    s.push(3);
    s.push(5);
    s.push(1);
    s.push(2);
    assert(s.min() == 1);
    assert(s.top() == 2);

    s.pop();
    s.pop();
    assert(s.min() == 3);
    assert(s.top() == 5);

    s.push(3);
    s.push(3);
    assert(s.min() == 3);
    s.pop();
    assert(s.min() == 3);

    MinStack s2;
    s2.push(42);
    assert(s2.min() == 42);
    assert(s2.top() == 42);

    MinStack s3;
    bool sawPopError = false;
    try {
        s3.pop();
    } catch (const runtime_error&) {
        sawPopError = true;
    }
    assert(sawPopError);

    bool sawMinError = false;
    try {
        s3.min();
    } catch (const runtime_error&) {
        sawMinError = true;
    }
    assert(sawMinError);

    cout << "All test cases passed ✅" << endl;
    return 0;
}
