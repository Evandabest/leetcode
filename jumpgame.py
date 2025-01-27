
# Leetcode 55: Jump Game

from typing import List

def canJump(self, nums: List[int]) -> bool:
        
    farthest = 0

    potential = 0

    for i in range(len(nums)):
        if i > potential:
            break
        potential = max(potential, i + nums[i])
        farthest = max(potential, farthest) 
            
    return farthest >= len(nums)-1