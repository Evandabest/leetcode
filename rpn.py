
# Leetcode 150. Evaluate Reverse Polish Notation

from typing import List

def evalRPN(self, tokens: List[str]) -> int:
        
        operations = ['-', '+', '/', '*']

        stack = []

        for i in tokens:
            if i in operations:
                if i == '-':
                    val1 = int(stack.pop())
                    val2 = int(stack.pop())
                    stack.append(val2 - val1)
                elif i == '+':
                    val1 = int(stack.pop())
                    val2 = int(stack.pop())
                    stack.append(val2 + val1)
                elif i == '/':
                    val1 = int(stack.pop())
                    val2 = int(stack.pop())
                    stack.append(int(val2/val1))
                elif i == '*':
                    val1 = int(stack.pop())
                    val2 = int(stack.pop())
                    stack.append(val1 * val2)
            else:
                stack.append(i)
        
        return int(stack[0])