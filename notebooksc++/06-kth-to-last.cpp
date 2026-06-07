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

// Find the value of the kth node from the end of the linked list
// Using fast and slow pointer approach
int kthToLast(ListNode* head, int k) {
    ListNode* fast = head;
    ListNode* slow = head;
    
    // Move fast pointer k steps ahead
    for (int i = 0; i < k; i++) {
        fast = fast->next;
    }
    
    // Move both pointers until fast reaches the end
    while (fast != nullptr) {
        fast = fast->next;
        slow = slow->next;
    }
    
    return slow->val;
}

// Helper function to create linked list from vector
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

// Helper function to clean up memory
void deleteLinkedList(ListNode* head) {
    while (head != nullptr) {
        ListNode* temp = head;
        head = head->next;
        delete temp;
    }
}

int main() {
    // Test case: 1 -> 2 -> 3 -> 4 -> 5
    ListNode* head = createLinkedList({1, 2, 3, 4, 5});
    
    assert(kthToLast(head, 1) == 5);  // kth to last (k=1) should be 5
    assert(kthToLast(head, 2) == 4);  // kth to last (k=2) should be 4
    assert(kthToLast(head, 3) == 3);  // kth to last (k=3) should be 3
    assert(kthToLast(head, 5) == 1);  // kth to last (k=5) should be 1
    
    deleteLinkedList(head);
    
    // Test case: single node list
    ListNode* head2 = createLinkedList({42});
    assert(kthToLast(head2, 1) == 42);
    deleteLinkedList(head2);
    
    cout << "All test cases passed ✅" << endl;
    return 0;
}
