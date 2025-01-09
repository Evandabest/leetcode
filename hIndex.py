# leetcode 274. H-Index

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        maxH = 0

        if len(citations) == 1 and citations[0] != 0:
            return 1
 
        for i in citations:
            h = i
            more = 0
            for j in citations:
                if j >= h:
                    more +=1
            
            print(more, h, maxH)
            if more >= h and h >= maxH:
                maxH = h
            elif more >= maxH and maxH <= h:
                maxH = more
        
        return maxH
