

#Leetcode 509. Fibonacci Number




def fib(self, n: int) -> int:
        
        mapfib = {0:0, 1:1}

        def find(n):
            if n in mapfib.keys():
                return mapfib[n]
            else:
                ans = find(n-1) + find(n-2)
                mapfib[n] = ans
                return ans
        
        return find(n)
