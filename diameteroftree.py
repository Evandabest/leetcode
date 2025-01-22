


# Leetcode 543. Diameter of Binary Tree

from typing import Optional

# failed attempt, 101/108 test cases passed

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def check(root): 
            if not(root.left) and not(root.right):
                return 1
            else:
                only1 = False
                if root.right and root.left:
                    return 1 + max(check(root.left), check(root.right))
                elif root.right:
                    return 1 + check(root.right)
                elif root.left:
                    return 1 + check(root.left)

        if root.right and root.left:
            ans = check(root.right) + check(root.left)
            print(check(root.right))
        elif root.right:
            ans = check(root.right)
        elif root.left:
            ans = check(root.left)
        else:
            return 0
        
        return ans