class MinStack:
    """支持 O(1) 时间获取最小值的栈。

    算法思路（双栈协同）：
        维护两个栈：
        - _data：正常存储所有压入的元素。
        - _min：辅助栈，栈顶始终是 _data 当前所有元素中的最小值。

        每次 push 时，若新元素 <= 辅助栈栈顶，则同步压入辅助栈；
        每次 pop 时，若弹出的元素等于辅助栈栈顶，则辅助栈同步弹出。
        这样 min() 只需返回辅助栈栈顶，始终是 O(1)。

    Complexity:
        push / pop / top / min: Time O(1)，Space O(n)。
    """

    def __init__(self) -> None:
        """初始化数据栈与辅助最小值栈。"""
        self._data: list[int] = []   # 主数据栈
        self._min:  list[int] = []   # 辅助栈：栈顶始终是当前最小值

    def push(self, val: int) -> None:
        """将元素压入栈，并同步维护辅助栈。

        Args:
            val (int): 待压入的整数。

        Note:
            当 val <= 当前最小值（或辅助栈为空）时，同步压入辅助栈，
            确保辅助栈栈顶始终反映最新的最小值。
        """
        self._data.append(val)
        # 辅助栈为空，或新值不大于当前最小值时才压入
        if not self._min or val <= self._min[-1]:
            self._min.append(val)

    def pop(self) -> None:
        """弹出栈顶元素，并同步维护辅助栈。

        Raises:
            IndexError: 栈为空时调用。

        Note:
            若弹出的元素恰好等于辅助栈栈顶，说明当前最小值被移除，
            辅助栈需同步弹出以还原上一个最小值。
        """
        if not self._data:
            raise IndexError("pop from empty stack")
        val = self._data.pop()
        if val == self._min[-1]:
            self._min.pop()

    def top(self) -> int:
        """返回栈顶元素，不弹出。

        Returns:
            int: 当前栈顶的整数值。

        Raises:
            IndexError: 栈为空时调用。
        """
        if not self._data:
            raise IndexError("top from empty stack")
        return self._data[-1]

    def min(self) -> int:
        """返回栈内所有元素的最小值，不弹出。

        Returns:
            int: 当前栈中的最小整数值。

        Raises:
            IndexError: 栈为空时调用。

        Complexity:
            Time: O(1) — 直接读取辅助栈栈顶。
        """
        if not self._min:
            raise IndexError("min from empty stack")
        return self._min[-1]


# ── 测试用例 ──────────────────────────────────────────────────

if __name__ == "__main__":
    s = MinStack()

    # 用例 1: 基本压栈与 min
    s.push(3)
    s.push(5)
    s.push(1)
    s.push(2)
    assert s.min() == 1,  "最小值应为 1"
    assert s.top() == 2,  "栈顶应为 2"

    # 用例 2: 弹出最小值后，min 应还原为上一个最小值
    s.pop()   # 弹出 2
    s.pop()   # 弹出 1（当前最小值）
    assert s.min() == 3,  "弹出 1 后最小值应还原为 3"
    assert s.top() == 5,  "栈顶应为 5"

    # 用例 3: 压入重复的最小值，两次弹出后 min 仍正确
    s.push(3)
    s.push(3)
    assert s.min() == 3,  "重复最小值时 min 应为 3"
    s.pop()
    assert s.min() == 3,  "弹出一个重复最小值后 min 仍应为 3"

    # 用例 4: 单元素栈
    s2 = MinStack()
    s2.push(42)
    assert s2.min() == 42, "单元素 min 应为 42"
    assert s2.top() == 42, "单元素 top 应为 42"

    # 用例 5: 空栈操作应抛出 IndexError
    s3 = MinStack()
    try:
        s3.pop()
        assert False, "空栈 pop 应抛出 IndexError"
    except IndexError:
        pass

    try:
        s3.min()
        assert False, "空栈 min 应抛出 IndexError"
    except IndexError:
        pass

    print("所有测试用例通过 ✅")
