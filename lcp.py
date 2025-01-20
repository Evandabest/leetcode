

# Leetcode 14. Longest Common Prefix

from typing import List

def longestCommonPrefix(self, strs: List[str]) -> str:
        
        p = 0

        common = ""

        shortest = strs[0]

        for i in strs:
            if len(i) < len(shortest):
                shortest = i
        
        while p < len(shortest):
            isTrue = True
            target = shortest[p]
            for i in strs:
                if i[p] != target:
                    isTrue = False
                    break
            
            if isTrue:
                common += shortest[p]
                p+=1
            else:
                break
        
        return common