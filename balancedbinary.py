

# Leetcode 110. Balanced Binary Tree (Bad solution i assume)


from typing import Optional


#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True
        def depth(root):
            if not root:
                return 0
            return 1 + max(depth(root.left), depth(root.right))

        def check(root):
            leftdepth = 0
            rightdepth = 0
            if not root:
                return
            if root.left:
                leftdepth = depth(root.left)
            if root.right:
                rightdepth = depth(root.right)
            
            if abs(leftdepth - rightdepth) > 1:
                self.isBalanced = False
            else:
                check(root.left)
                check(root.right)
        check(root)

        return self.isBalanced