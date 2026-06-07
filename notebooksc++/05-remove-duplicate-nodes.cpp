#include <iostream>
#include <unordered_set>
#include <vector>
#include <cassert>

using namespace std;

// Definition for singly-linked list
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int val = 0, ListNode* next = nullptr) : val(val), next(next) {}
};

// Remove duplicate nodes from linked list
ListNode* removeDuplicateNodes(ListNode* head) {
    if (head == nullptr) {
        return head;
    }
    
    unordered_set<int> visited;
    visited.insert(head->val);
    ListNode* curr = head;
    
    while (curr != nullptr && curr->next != nullptr) {
        if (visited.count(curr->next->val) > 0) {
            curr->next = curr->next->next;
        } else {
            visited.insert(curr->next->val);
            curr = curr->next;
        }
    }
    
    return head;
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

// Helper function to convert linked list to vector
vector<int> linkedListToVector(ListNode* head) {
    vector<int> result;
    ListNode* curr = head;
    
    while (curr != nullptr) {
        result.push_back(curr->val);
        curr = curr->next;
    }
    
    return result;
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
    // Test 1: list with duplicates 1 -> 2 -> 3 -> 3 -> 2 -> 1
    ListNode* head1 = createLinkedList({1, 2, 3, 3, 2, 1});
    ListNode* result1 = removeDuplicateNodes(head1);
    vector<int> vec1 = linkedListToVector(result1);
    vector<int> expected1 = {1, 2, 3};
    assert(vec1 == expected1);
    deleteLinkedList(result1);
    
    // Test 2: list with no duplicates 1 -> 2 -> 3
    ListNode* head2 = createLinkedList({1, 2, 3});
    ListNode* result2 = removeDuplicateNodes(head2);
    vector<int> vec2 = linkedListToVector(result2);
    vector<int> expected2 = {1, 2, 3};
    assert(vec2 == expected2);
    deleteLinkedList(result2);
    
    // Test 3: empty list
    ListNode* head3 = removeDuplicateNodes(nullptr);
    assert(head3 == nullptr);
    
    // Test 4: single element
    ListNode* head4 = createLinkedList({5});
    ListNode* result4 = removeDuplicateNodes(head4);
    vector<int> vec4 = linkedListToVector(result4);
    vector<int> expected4 = {5};
    assert(vec4 == expected4);
    deleteLinkedList(result4);
    
    cout << "All test cases passed ✅" << endl;
    return 0;
}
