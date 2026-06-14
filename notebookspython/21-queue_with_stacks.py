"""
实现说明：
通过两个栈 (in_stack, out_stack) 模拟队列的先进先出 (FIFO) 特性。
核心逻辑是“延迟搬运”：仅当 out_stack 为空时，才将 in_stack 的数据
倒序压入 out_stack，从而实现 O(1) 的均摊时间复杂度。
"""
class MyQueue:
    def __init__(self):
        # 使用 Python 的 list 作为栈
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.peek()  # 确保 out_stack 有数据
        return self.out_stack.pop()

    def peek(self) -> int:
        # 只有当 out_stack 为空时，才将 in_stack 的数据倒过来
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack