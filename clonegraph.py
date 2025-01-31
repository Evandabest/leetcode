
# Leetcode: 133. Clone Graph

"""
# Definition for a Node.

"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return 
        nodes = dict()

        def dfs(node):
            if node and node.val in nodes.keys():
                return
            elif node:
                neighbors = []
                for i in node.neighbors:
                    neighbors.append(i.val)
                nodes[node.val] = neighbors
                for i in node.neighbors:
                    dfs(i)
            
        
        dfs(node)

        #halfway done

        def construct(val):
            for i in nodes[val]:
                constructed[val].neighbors.append(constructed[i])

        
        make = set(nodes.keys())
        constructed = dict()

        for i in make:
            constructed[i] = Node(i)

        for i in make:
            construct(i)
        
        return constructed[node.val]