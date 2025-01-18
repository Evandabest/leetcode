
#leetcode 1137. N-th Tribonacci Number


def tribonacci(self, n: int) -> int:
        
        trimap = {0:0, 1:1, 2:1}

        def trib(n):
            if n in trimap.keys():
                return trimap[n]
            else:
                ans = trib(n-1) + trib(n-2) + trib(n-3)
                trimap[n] = ans
                return ans

        return trib(n)