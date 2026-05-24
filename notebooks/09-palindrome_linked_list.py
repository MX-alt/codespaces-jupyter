class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """判断单链表是否为回文序列。

    算法思路：
        将链表节点值依次写入数组，再用双指针从两端向中间比对。
        空链表和单节点链表均视为回文。
    """

    def isPalindrome(self, head: ListNode) -> bool:
        """判断以 head 为头节点的单链表是否构成回文序列。

        Args:
            head (ListNode | None): 链表头节点；传入 None 表示空链表。

        Returns:
            bool: 链表节点值从左到右与从右到左完全相同时返回 True，否则返回 False。

        Complexity:
            Time:  O(n) — 遍历链表一次写入数组，双指针比对最多再遍历一次。
            Space: O(n) — 额外数组存储 n 个节点值。

        Examples:
            >>> s = Solution()
            >>> s.isPalindrome(create_linked_list([1, 2, 2, 1]))
            True
            >>> s.isPalindrome(create_linked_list([1, 2, 3, 1]))
            False
            >>> s.isPalindrome(None)
            True
        """
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

    # ── 边界测试用例 ──────────────────────────────────────────

    # 用例 3: 空链表 → True（空序列视为回文）
    assert solver.isPalindrome(None) == True, "空链表应返回 True"

    # 用例 4: 单节点 [7] → True（奇数长度，只有一个元素）
    assert solver.isPalindrome(create_linked_list([7])) == True, "单节点应返回 True"

    # 用例 5: 奇数长度回文 [1, 2, 1] → True
    assert solver.isPalindrome(create_linked_list([1, 2, 1])) == True, "[1,2,1] 应返回 True"

    # 用例 6: 偶数长度回文 [1, 2, 2, 1] → True
    assert solver.isPalindrome(create_linked_list([1, 2, 2, 1])) == True, "[1,2,2,1] 应返回 True"

    # 用例 7: 偶数长度非回文 [1, 2, 3, 1] → False
    assert solver.isPalindrome(create_linked_list([1, 2, 3, 1])) == False, "[1,2,3,1] 应返回 False"

    print("所有边界测试用例通过 ✅")