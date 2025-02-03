

#Leetcode #34. Find First and Last Position of Element in Sorted Array

from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    
    start = 0
    end = len(nums) -1

    ans = [-1,-1]

    if len(nums) == 1 and nums[0] == target:
        ans[0] = 0
        ans[1] = 0
        return ans

    while start <= end:
        mid = start + (end - start)//2
        if nums[mid] == target:
            ans[0] = mid
            break
        elif nums[mid] < target:
            start = mid+1
        else:
            end = mid - 1

    if ans[0] == -1 and ans[1] == -1:
        return ans

    
    def checkL(pos):
        if pos > 0 :
            if nums[pos-1] == target:
                ans[0] = pos-1
                checkL(pos-1)
    
    def checkR(pos):
        if pos < len(nums)-1:
            if nums[pos+1] == target:
                ans[1] = pos+1
                checkR(pos+1)
        
    checkL(mid)
    checkR(mid)
    print(ans)

    if ans[0] == -1:
        ans[0] = mid
    
    if ans[1] == -1:
        ans[1] = mid

    return ans

nums = [0,0,1,1,1,2,2,3,3,3,4,4,4,4,5,5,6,6,6,8,10,10]
target = 4
print(nums, target)
print(searchRange(nums, target))