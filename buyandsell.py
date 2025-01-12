

#Leetcode 121. Best Time to Buy and Sell Stock

from typing import List

def maxProfit(self, prices: List[int]) -> int:
        maxi = 0

        p1 = 0
        p2 = 1

        while p2 < len(prices):
            '''
            if prices[p1] == 0:
                high = max(prices[p1+1:len(prices)])
                if high > maxi:
                    return high
                break

            elif prices[p2] == 0 and p2 != len(prices)-1:
                high = max(prices[p2+1:len(prices)])
                if high > maxi:
                    return high
                break
            '''

            difference = prices[p2] - prices[p1]
            if difference > 0:
                if difference > maxi:
                    maxi = difference
            elif difference < 0:
                p1 = p2
            
            p2 +=1

            print(p1, p2, difference)
        return maxi