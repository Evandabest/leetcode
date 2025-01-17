
# leetcode 70. Climbing Stairs

def climbStairs(self, n: int) -> int:
        
        """
        notes:
        n =...
        1 -> 1
        2 -> 2
        3 -> 3
        4 -> 1, 2, 
        ITS JUST FIBONACCI BRUHHH
        """

        hashmap = {
            0:1,
            1: 1
        }

        def fib(n):
            if n in hashmap.keys():
                return hashmap[n]
            else:
                ans = fib(n-1) + fib(n-2)
                hashmap[n] = ans
                return ans

        return fib(n)