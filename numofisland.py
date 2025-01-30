

# Leetcode 200. Number of Islands

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        self.seen = set()
        self.islands = 0

        def dfs(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or (x, y) in self.seen or grid[x][y] == "0":
                return

            self.seen.add((x,y))

            dfs(x,y + 1)
            dfs(x+1, y)
            dfs(x,y - 1)
            dfs(x-1, y)
            

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in self.seen:
                    continue
                if grid[i][j] == "1":
                    self.islands +=1
                    dfs(i,j)

        return self.islands




