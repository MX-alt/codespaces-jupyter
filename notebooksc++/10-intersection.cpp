#include <iostream>
#include <unordered_set>
#include <vector>
#include <cassert>

using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int val = 0, ListNode* next = nullptr) : val(val), next(next) {}
};

ListNode* getIntersectionNodeSet(ListNode* headA, ListNode* headB) {
    if (headA == nullptr || headB == nullptr) return nullptr;
    unordered_set<ListNode*> seen;
    while (headA != nullptr) {
        seen.insert(headA);
        headA = headA->next;
    }
    while (headB != nullptr) {
        if (seen.count(headB) > 0) {
            return headB;
        }
        headB = headB->next;
    }
    return nullptr;
}

ListNode* getIntersectionNode(ListNode* headA, ListNode* headB) {
    if (headA == nullptr || headB == nullptr) return nullptr;
    ListNode* a = headA;
    ListNode* b = headB;
    while (a != b) {
        a = (a == nullptr) ? headB : a->next;
        b = (b == nullptr) ? headA : b->next;
    }
    return a;
}

ListNode* buildSharedTail(const vector<int>& vals) {
    if (vals.empty()) return nullptr;
    ListNode* head = new ListNode(vals[0]);
    ListNode* curr = head;
    for (size_t i = 1; i < vals.size(); i++) {
        curr->next = new ListNode(vals[i]);
        curr = curr->next;
    }
    return head;
}

ListNode* buildPrefix(ListNode* tail, const vector<int>& vals) {
    if (vals.empty()) return tail;
    ListNode* head = new ListNode(vals[0]);
    ListNode* curr = head;
    for (size_t i = 1; i < vals.size(); i++) {
        curr->next = new ListNode(vals[i]);
        curr = curr->next;
    }
    curr->next = tail;
    return head;
}

void deleteList(ListNode* head, ListNode* stop = nullptr) {
    while (head != nullptr && head != stop) {
        ListNode* temp = head;
        head = head->next;
        delete temp;
    }
}

void deleteTree(ListNode* head) {
    while (head != nullptr) {
        ListNode* temp = head;
        head = head->next;
        delete temp;
    }
}

int main() {
    assert(getIntersectionNode(nullptr, nullptr) == nullptr);
    assert(getIntersectionNodeSet(nullptr, nullptr) == nullptr);

    ListNode* single = new ListNode(1);
    assert(getIntersectionNode(nullptr, single) == nullptr);
    assert(getIntersectionNode(single, nullptr) == nullptr);

    ListNode* shared = buildSharedTail({8, 4, 5});
    ListNode* headA = buildPrefix(shared, {4, 1});
    ListNode* headB = buildPrefix(shared, {5, 6, 1});

    assert(getIntersectionNode(headA, headB) == shared);
    assert(getIntersectionNodeSet(headA, headB) == shared);
    assert(getIntersectionNode(shared, shared) == shared);

    ListNode* c = buildSharedTail({1, 2, 3});
    ListNode* d = buildSharedTail({4, 5, 6});
    assert(getIntersectionNode(c, d) == nullptr);

    deleteList(headA, shared);
    deleteList(headB, shared);
    deleteTree(shared);
    deleteTree(c);
    deleteTree(d);
    delete single;

    cout << "All test cases passed ✅" << endl;
    return 0;
}
