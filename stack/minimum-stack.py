from typing import Optional


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> Optional[int]:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> Optional[int]:
        if self.min_stack:
            return self.min_stack[-1]
        return None
