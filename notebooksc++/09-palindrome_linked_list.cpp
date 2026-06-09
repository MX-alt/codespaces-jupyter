#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int val = 0, ListNode* next = nullptr) : val(val), next(next) {}
};

bool isPalindrome(ListNode* head) {
    vector<int> vals;
    while (head != nullptr) {
        vals.push_back(head->val);
        head = head->next;
    }
    int left = 0;
    int right = static_cast<int>(vals.size()) - 1;
    while (left < right) {
        if (vals[left] != vals[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
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

void deleteLinkedList(ListNode* head) {
    while (head != nullptr) {
        ListNode* temp = head;
        head = head->next;
        delete temp;
    }
}

int main() {
    assert(isPalindrome(nullptr) == true);

    ListNode* head1 = createLinkedList({7});
    assert(isPalindrome(head1) == true);
    deleteLinkedList(head1);

    ListNode* head2 = createLinkedList({1, 2, 1});
    assert(isPalindrome(head2) == true);
    deleteLinkedList(head2);

    ListNode* head3 = createLinkedList({1, 2, 2, 1});
    assert(isPalindrome(head3) == true);
    deleteLinkedList(head3);

    ListNode* head4 = createLinkedList({1, 2, 3, 1});
    assert(isPalindrome(head4) == false);
    deleteLinkedList(head4);

    cout << "All test cases passed ✅" << endl;
    return 0;
}
