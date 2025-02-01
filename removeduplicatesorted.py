

# Leetcode 26. Remove Duplicates from Sorted Array

from typing import List

def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
 
        p1 = 1
        
        while p1 < len(nums):
            if nums[p1] == nums[p1 -1]:
                nums.pop(p1)
            else:
                p1 +=1        

        return len(nums)