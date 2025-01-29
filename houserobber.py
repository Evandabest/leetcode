
# LeetCode 198. House Robber

#First DP bottom up approach problem solved!!!!

from typing import List

def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        dp = [0] * (len(nums))

        dp[0] = nums[0]
        dp[1] = max(dp[0],nums[1])
        #maximum = max(dp[0], dp[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            #maximum = max(maximum, dp[i])
        
        return dp[-1]