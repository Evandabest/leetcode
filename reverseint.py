

# Leetcode 7: Reverse Integer

def reverse(self, x: int) -> int:
        
        negative = True if x < 0 else False

        nums = list(str(abs(x)))

        if len(nums) == 1:
            return -int(nums[0]) if negative else int(nums[0])
        
        ans = int("".join(nums[::-1]).lstrip("0"))

        if ans > 2 ** 31 or ans < -2**31:
            return 0

        return -ans if negative else ans