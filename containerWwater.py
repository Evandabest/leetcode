# Leetcode: 11. Container With Most Water

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        l = 0

        max = 0

        while l < len(height) - 1:
            currHeight = height[l]
            r = l + 1
            while r < len(height):
                least = min(currHeight, height[r])
                area = least * (r - l)
                if area > max:
                    max = area
                r+=1
            l +=1

        return max
        """

        l = 0
        r = len(height) - 1

        max = 0

        while l < r:
            least = min(height[l], height[r])
            distance = r - l
            area = least * distance
            if area > max:
                max = area
            
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        
        return max