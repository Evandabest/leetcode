
#Leet code: 217. Contains Duplicate
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hashset = set()

        size = 0

        for i in nums:
            hashset.add(i)
            newSize = len(hashset)
            if size == newSize:
                return True
            else:
                size+= 1
            
        return False