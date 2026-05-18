from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def kthToLast(self, head: Optional[ListNode], k: int) -> int:
        fast = head
        slow = head
        
        # 1. 让快指针先往前走 k 步
        for _ in range(k):
            fast = fast.next
            
        # 2. 快慢指针同时一步一步往前走，直到快指针走出链表（变成 None）
        while fast:
            fast = fast.next
            slow = slow.next
            
        # 3. 此时 slow 刚好停在倒数第 k 个节点上，返回它的值
        return slow.val

# 辅助函数：方便测试
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

if __name__ == "__main__":
    # 创建链表：1 -> 2 -> 3 -> 4 -> 5
    head = create_linked_list([1, 2, 3, 4, 5])
    
    sol = Solution()
    
    # 比如：找倒数第 2 个节点（期望结果应该是 4）
    result = sol.kthToLast(head, 2)
    print("倒数第 2 个节点的值是:", result)