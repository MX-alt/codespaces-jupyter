#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

// Definition for singly-linked list
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int val = 0, ListNode* next = nullptr) : val(val), next(next) {}
};

// Delete node in-place by copying next node's value and skipping it.
void deleteNode(ListNode* node) {
    if (node == nullptr || node->next == nullptr) {
        return;
    }
    node->val = node->next->val;
    node->next = node->next->next;
}

ListNode* createLinkedList(const vector<int>& values) {
    if (values.empty()) {
        return nullptr;
    }
    ListNode* head = new ListNode(values[0]);
    ListNode* curr = head;
    for (size_t i = 1; i < values.size(); i++) {
        curr->next = new ListNode(values[i]);
        curr = curr->next;
    }
    return head;
}

vector<int> linkedListToVector(ListNode* head) {
    vector<int> result;
    while (head != nullptr) {
        result.push_back(head->val);
        head = head->next;
    }
    return result;
}

void deleteLinkedList(ListNode* head) {
    while (head != nullptr) {
        ListNode* temp = head;
        head = head->next;
        delete temp;
    }
}

int main() {
    ListNode* head1 = createLinkedList({4, 5, 1, 9});
    ListNode* nodeToDelete = head1->next;
    deleteNode(nodeToDelete);
    assert(linkedListToVector(head1) == vector<int>({4, 1, 9}));
    deleteLinkedList(head1);

    ListNode* head2 = createLinkedList({1, 2, 3});
    ListNode* mid = head2->next;
    deleteNode(mid);
    assert(linkedListToVector(head2) == vector<int>({1, 3}));
    deleteLinkedList(head2);

    cout << "All test cases passed ✅" << endl;
    return 0;
}
