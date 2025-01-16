

# Leetcode 3. Longest Substring Without Repeating Characters



def lengthOfLongestSubstring(self, s: str) -> int:
    
    if len(s) == 1:
        return 1


    hashset = set()
    
    ans = 0

    p1 = 0
    p2 = 1

    localMax = 0

    while p2 < len(s) and p1 < len(s):
        length = len(hashset)
        hashset.add(s[p1])
        if len(hashset) != length:
            localMax += 1
            ans = max(localMax, ans)
        
        length = max(length, len(hashset))
        hashset.add(s[p2])
        if len(hashset) != length:
            localMax += 1
            ans = max(localMax, ans)
            p2+=1
        else:
            localMax -= 1
            hashset.remove(s[p1])
            p1 = p1+1
            if p1 == p2:
                p2 +=1
            

    return ans