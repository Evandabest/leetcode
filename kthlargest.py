

# leetcode 215. Kth Largest Element in an Array
from typing import List

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []

        for i in nums:
            heapq.heappush(heap, -i)

    
        ans = 0
        for i in range(k):
            ans = -heapq.heappop(heap)
        
        return ans