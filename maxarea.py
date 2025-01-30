
# Leetcode 695. Max Area of Island

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        self.seen = set()

        maxArea = 0

        def dfs(x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or (x,y) in self.seen:
                return 0
                
            if grid[x][y] == 0:
                return 0
            
            self.seen.add((x,y))
            
            return 1 + (dfs(x +1, y) + dfs(x, y+1) + dfs(x-1, y) + dfs(x, y-1))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = dfs(i,j)
                    print(area)
                    maxArea = max(area, maxArea)
                
        return maxArea