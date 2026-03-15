class MyQueue:
    def __init__(self):
        self._in_stack = []
        self._out_stack = []

    def push(self, x: int) -> None:
        self._in_stack.append(x)

    def pop(self) -> int:
        if not self._out_stack:
            while self._in_stack:
                self._out_stack.append(self._in_stack.pop())
        return self._out_stack.pop()

    def peek(self) -> int:
        if not self._out_stack:
            while self._in_stack:
                self._out_stack.append(self._in_stack.pop())
        return self._out_stack[-1]

    def empty(self) -> bool:
        return not self._in_stack and not self._out_stack
