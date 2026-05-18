from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNode(self, node: ListNode) -> None:
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

if __name__ == "__main__":
    # 1. 组装链表: 4 -> 5 -> 1 -> 9
    head = ListNode(4)
    node_to_delete = ListNode(5)  # 👈 假设我们要删掉这个节点 5
    
    head.next = node_to_delete
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(9)

    print("削除前のチェーン:")
    curr = head
    while curr:
        print(curr.val, end=" -> " if curr.next else "\n")
        curr = curr.next

    # 2. 调用算法：注意！我们只把 node_to_delete（节点5）传进去
    sol = Solution()
    sol.deleteNode(node_to_delete)

    print("\n削除後のチェーン:")
    curr = head
    while curr:
        print(curr.val, end=" -> " if curr.next else "\n")
        curr = curr.next