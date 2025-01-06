

import typing

# Leetcode #49: Group Anagrams


class Solution:
    def groupAnagrams(self, strs: typing.List[str]) -> typing.List[typing.List[str]]:

        map = {}
        
        for i in strs:
            chars = list(i)
            sortedChars = sorted(chars)
            joined = ("").join(sortedChars)
            
            if joined in map.keys():
                map[joined].append(i)
            else:
                map[joined] = [i]
        
        return list(map.values())