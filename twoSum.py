
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {}

        for i in range(len(nums)):
            if target - nums[i] in map.keys():
                return [i, map[target - nums[i]]]
            else:
                map[nums[i]] = i