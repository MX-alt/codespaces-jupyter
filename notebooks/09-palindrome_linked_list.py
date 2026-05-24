class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 1. 一路从前往后读，把所有值存进数组
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
            
        # 2. 此时 vals 已经是像 [1, 2, 2, 1] 这样的数组了
        # 我们可以直接用双指针，从“两头向中间”靠拢比对
        left = 0
        right = len(vals) - 1
        
        while left < right:
            if vals[left] != vals[right]:
                return False  # 一旦发现不对称，立刻返回 False
            left += 1         # 左指针往右走
            right -= 1        # 右指针往左走
            
        return True

def create_linked_list(arr):
    """辅助函数：用数组快速生成链表"""
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

if __name__ == "__main__":
    solver = Solution()
    
    # 测试用例 1: [1, 2, 2, 1] 是回文
    head1 = create_linked_list([1, 2, 2, 1])
    print(f"测试用例 1 结果: {solver.isPalindrome(head1)}") # 应该输出 True
    
    # 测试用例 2: [1, 2] 不是回文
    head2 = create_linked_list([1, 2])
    print(f"测试用例 2 结果: {solver.isPalindrome(head2)}") # 应该输出 False