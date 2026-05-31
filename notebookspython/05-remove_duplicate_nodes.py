from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeDuplicateNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        visited = {head.val}
        curr = head

        while curr and curr.next:
            if curr.next.val in visited:
                curr.next = curr.next.next
            else:
                visited.add(curr.next.val)
                curr = curr.next
        return head
    
def create_linked_list(values):
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
        
    return head

if __name__ == "__main__":
    # 创建链表 1 -> 2 -> 3 -> 3 -> 2 -> 1
    head = create_linked_list([1, 2, 3, 3, 2, 1])
    
    # 创建类的实例
    sol = Solution()
    
    # 移除重复节点
    new_head = sol.removeDuplicateNodes(head)

    # 打印结果链表
    curr = new_head
    while curr:
        print(curr.val, end=" -> " if curr.next else "")
        curr = curr.next