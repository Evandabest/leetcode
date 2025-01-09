
# Leetcode 20: Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:

        map = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }

        if len(s) %2 != 0:
            return False

        stack = []

        for i in range(len(s)):
            if s[i] in map.values():
                stack.append(s[i])
            elif stack and stack[len(stack)-1] == map[s[i]]:
                stack.pop(len(stack)-1)
            else:
                stack.append(s[i])
        
        return len(stack) == 0