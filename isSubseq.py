
# Problem: 392. Is Subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) == 0:
            return True
        
        if len(t) == 0:
            return False

        p1, p2 = 0, 0

        while p1 < len(s):
            print(p1,p2)
            if s[p1] == t[p2]:
                p1+=1
                if p2 < len(t)-1:
                    p2+=1
                else:
                    break
            elif p2 < len(t)-1:
                p2+=1
            else:
                return False
        
        return p1 == len(s)
