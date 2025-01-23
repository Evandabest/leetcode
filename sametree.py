

# LeetCode 100. Same Tree


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        stack1 = []
        stack2 = []

        def addtoStack(root, stack):
            if not root:
                return
            else:
                stack.append(root.val)
            
            if root.left:
                print(root.val)
                stack.append(addtoStack(root.left, stack)) 
            else:
                stack.append("None")

            if root.right:
                stack.append(addtoStack(root.right, stack))
            else:
                stack.append("None")

        addtoStack(p, stack1)
        addtoStack(q, stack2)
        
        if len(stack1) != len(stack2):
            return False

        for i in range(len(stack1)):
            val1 = stack1.pop()
            val2 = stack2.pop()
            if val1 != val2:
                return False
        
        return True
