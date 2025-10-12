from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token in operators:
                op2 = stack.pop()
                op1 = stack.pop()
                if token == "+":
                    stack.append(op1 + op2)
                elif token == "-":
                    stack.append(op1 - op2)
                elif token == "*":
                    stack.append(op1 * op2)
                elif token == "/":
                    stack.append(int(op1 / op2))
            else:
                stack.append(int(token))

        return stack[0]
