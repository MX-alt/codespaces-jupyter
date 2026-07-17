# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 创建两个哑节点
        small_head = ListNode(0)
        large_head = ListNode(0)
        
        small = small_head
        large = large_head
        
        curr = head
        while curr:
            if curr.val < x:
                small.next = curr
                small = small.next
            else:
                large.next = curr
                large = large.next
            curr = curr.next
        
        # 将 large 链表结尾置空，防止环
        large.next = None
        # 连接两个链表
        small.next = large_head.next
        
        return small_head.next
