


#Leetcode 66. Plus One

from typing import List

def plusOne(self, digits: List[int]) -> List[int]:
        
        digits[len(digits)-1] += 1

        i = len(digits) -1
        while i >= 0:

            if digits[i] >= 10:
                digits[i] -= 10
                if digits[i-1]:
                    digits[i-1] +=1
                else:
                    digits.insert(0, 1)
            i -= 1
        
        return digits
