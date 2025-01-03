#leetcode 242. Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashmap = dict()

        for i in s:
            if i in hashmap.keys():
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        for j in t:
            if j in hashmap.keys() and hashmap[j] > 0:
                hashmap[j] -= 1
            else:
                return False
        
        return not(max(hashmap.values()) > 0)

        #space complexity: O(n)

        #time complexity: 0(n)
        

        