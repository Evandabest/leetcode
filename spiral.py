
#Leetcode #54. Spiral Matrix

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        topb = 0
        rightb = len(matrix[0])
        bottomb = len(matrix) 
        leftb = 0

        order = []

        i = 0
        j = 0
        
        while bottomb >= topb and leftb <= rightb:

            if rightb-leftb == 0:
                break

            if bottomb-topb == 0:
                break
            
            while j < rightb:
                order.append(matrix[i][j])
                print("here1")
                j += 1
            j-=1
            i+=1
            

            while i < bottomb:
                order.append(matrix[i][j])
                print("her2")
                i += 1
            i-=1
            j-=1

            print(rightb, leftb)
            if rightb-leftb == 1:
                break

            if bottomb-topb == 1:
                break

            while j > leftb:
                order.append(matrix[i][j])
                print("here3")
                j -= 1


            while i > topb:
                order.append(matrix[i][j])
                print("here4")
                i -= 1
            i+=1
            j+=1

            topb +=1
            rightb-= 1
            leftb +=1
            bottomb -=1

        return order

'''
test = [
    [2,5,8],
    [4,0,-1]]

'''

test = [[1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15]]

problem = Solution()

print(problem.spiralOrder(test))