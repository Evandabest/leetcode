#leetcode 347. Top K Frequent Elements

from typing import List

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        map = {}
        ans = []

        for i in nums:
            if i in map.keys():
                map[i] +=1
            else:
                map[i] = 1
        
        keys = list(map.keys())
        values = list(map.values())
        print(map)

        heap = []
        for j in range(len(keys)):
            heapq.heappush(heap, (-values[j], keys[j]))
            #negate values bc we want max heap
  
        for j in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans