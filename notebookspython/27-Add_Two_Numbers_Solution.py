# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        curr = dummy_head
        carry = 0
        
        # 当 l1 或 l2 没遍历完，或者还有进位时，继续循环
        while l1 or l2 or carry:
            # 获取当前节点的值，如果为空则补 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # 计算当前位相加的总和（含进位）
            total = val1 + val2 + carry
            
            # 更新进位（商）
            carry = total // 10
            # 当前位的值（余数）
            new_val = total % 10
            
            # 创建新节点并连到结果链表上
            curr.next = ListNode(new_val)
            
            # 移动指针
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return dummy_head.next
