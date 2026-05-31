class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ── 解法一：暴力双重循环 ───────────────────────────────────────

class Solution:
    """找出两条单链表的相交节点（按节点引用，而非节点值）。

    算法思路：
        将两条链表的节点对象分别收集进两个列表。
        以较短列表为外层循环，在较长列表中逐一比对节点引用，
        第一个引用相同的节点即为交点。
    """

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        """返回两条链表的第一个相交节点，不相交则返回 None。

        Args:
            headA (ListNode | None): 链表 A 的头节点。
            headB (ListNode | None): 链表 B 的头节点。

        Returns:
            ListNode | None: 第一个相交节点的引用；若不相交返回 None。

        Complexity:
            Time:  O(m * n) — 外层遍历短链表 O(min(m,n))，内层遍历长链表 O(max(m,n))。
            Space: O(m + n) — 两个列表各存储一条链表的全部节点引用。

        Examples:
            >>> s = Solution()
            >>> shared = build_shared_tail([8, 4, 5])
            >>> headA = build_prefix([4, 1], shared)
            >>> headB = build_prefix([5, 6, 1], shared)
            >>> s.getIntersectionNode(headA, headB).val
            8
            >>> s.getIntersectionNode(None, None) is None
            True
        """
        if not headA or not headB:
            return None

        # 1. 收集两条链表的所有节点引用
        nodes_a, nodes_b = [], []
        curr = headA
        while curr:
            nodes_a.append(curr)
            curr = curr.next
        curr = headB
        while curr:
            nodes_b.append(curr)
            curr = curr.next

        # 2. 以较短列表为外层，在较长列表中逐一比对引用
        short, long = (nodes_a, nodes_b) if len(nodes_a) <= len(nodes_b) else (nodes_b, nodes_a)
        for node in short:
            if node in long:        # list.__contains__ 按引用比对，O(n)
                return node

        return None


# ── 解法二：哈希集合 ──────────────────────────────────────────

class SolutionSet:
    """找出两条单链表的相交节点（按节点引用，而非节点值）。

    算法思路：
        先将链表 A 的所有节点引用存入 set。
        再遍历链表 B，第一个出现在 set 中的节点即为交点。
        set 的查找是 O(1)，将整体时间从 O(m*n) 降至 O(m+n)。
    """

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        """返回两条链表的第一个相交节点，不相交则返回 None。

        Args:
            headA (ListNode | None): 链表 A 的头节点。
            headB (ListNode | None): 链表 B 的头节点。

        Returns:
            ListNode | None: 第一个相交节点的引用；若不相交返回 None。

        Complexity:
            Time:  O(m + n) — 遍历 A 建集合 O(m)，遍历 B 查集合 O(n)。
            Space: O(m)     — set 存储链表 A 的全部节点引用。

        Examples:
            >>> s = SolutionSet()
            >>> shared = build_shared_tail([8, 4, 5])
            >>> headA = build_prefix([4, 1], shared)
            >>> headB = build_prefix([5, 6, 1], shared)
            >>> s.getIntersectionNode(headA, headB).val
            8
            >>> s.getIntersectionNode(None, None) is None
            True
        """
        if not headA or not headB:
            return None

        # 1. 将链表 A 的所有节点引用存入 set
        seen = set()
        curr = headA
        while curr:
            seen.add(curr)
            curr = curr.next

        # 2. 遍历链表 B，第一个命中 set 的节点即为交点
        curr = headB
        while curr:
            if curr in seen:        # set 查找 O(1)
                return curr
            curr = curr.next

        return None


# ── 解法三：双指针对齐法 ──────────────────────────────────────

class SolutionTwoPointer:
    """找出两条单链表的相交节点（按节点引用，而非节点值）。

    算法思路：
        两条链表若相交，尾节点必然相同。
        设链表 A 长度为 m，链表 B 长度为 n，令两个指针分别从头出发：
        - 指针走完自己的链表后，跳到对方链表的头部继续走。
        - 经过 m + n 步后，两指针必然在交点处相遇（或同时到达 None，表示不相交）。
        无需额外空间，也不修改原链表。
    """

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        """返回两条链表的第一个相交节点，不相交则返回 None。

        Args:
            headA (ListNode | None): 链表 A 的头节点。
            headB (ListNode | None): 链表 B 的头节点。

        Returns:
            ListNode | None: 第一个相交节点的引用；若不相交返回 None。

        Complexity:
            Time:  O(m + n) — 两个指针各自最多走 m + n 步。
            Space: O(1)     — 只使用两个指针，不依赖额外数据结构。

        Examples:
            >>> s = SolutionTwoPointer()
            >>> shared = build_shared_tail([8, 4, 5])
            >>> headA = build_prefix([4, 1], shared)
            >>> headB = build_prefix([5, 6, 1], shared)
            >>> s.getIntersectionNode(headA, headB).val
            8
            >>> s.getIntersectionNode(None, None) is None
            True
        """
        if not headA or not headB:
            return None

        a, b = headA, headB
        # 两指针同步前进；走完本链表后切换到对方链表头
        # 若相交：经过 m+n 步在交点相遇
        # 若不相交：经过 m+n 步同时变为 None，退出循环
        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a  # 交点节点，或 None


# ── 辅助函数 ──────────────────────────────────────────────────

def build_shared_tail(arr: list) -> ListNode | None:
    """构造共享尾段链表，返回头节点。"""
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def build_prefix(arr: list, tail: ListNode | None) -> ListNode | None:
    """在 tail 前面拼接 arr 作为前缀，返回新链表头节点。"""
    if not arr:
        return tail
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    curr.next = tail  # 接上共享尾段
    return head


# ── 测试用例（三个解法共用相同场景）────────────────────────────

def run_tests(solver, label: str):
    # 用例 1: 两条链表均为空 → None
    assert solver.getIntersectionNode(None, None) is None, \
        f"[{label}] 双空链表应返回 None"

    # 用例 2: 一条为空，另一条非空 → None
    single = build_shared_tail([1])
    assert solver.getIntersectionNode(None, single) is None, \
        f"[{label}] A 为空应返回 None"
    assert solver.getIntersectionNode(single, None) is None, \
        f"[{label}] B 为空应返回 None"

    # 用例 3: 两条链表相交，交点在中间，前缀长度不等
    # A: 4 → 1 ─┐
    #             8 → 4 → 5
    # B: 5 → 6 → 1 ─┘
    intersection_node = build_shared_tail([8, 4, 5])
    headA = build_prefix([4, 1], intersection_node)
    headB = build_prefix([5, 6, 1], intersection_node)
    result = solver.getIntersectionNode(headA, headB)
    assert result is intersection_node, f"[{label}] 应返回交点节点引用"
    assert result.val == 8, f"[{label}] 交点节点值应为 8"

    # 用例 4: 两条链表在头节点就相交（完全共享）
    only_node = build_shared_tail([42])
    assert solver.getIntersectionNode(only_node, only_node) is only_node, \
        f"[{label}] 完全共享时应返回头节点"

    # 用例 5: 两条链表不相交
    headC = build_shared_tail([1, 2, 3])
    headD = build_shared_tail([4, 5, 6])
    assert solver.getIntersectionNode(headC, headD) is None, \
        f"[{label}] 不相交链表应返回 None"

    print(f"[{label}] 所有测试用例通过 ✅")


if __name__ == "__main__":
    run_tests(Solution(),           "解法一：暴力双重循环")
    run_tests(SolutionSet(),        "解法二：哈希集合")
    run_tests(SolutionTwoPointer(), "解法三：双指针对齐")
