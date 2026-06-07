class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        p1 = 0
        p2 = 0

        seen = set()
        res = 0

        for c in s:
            while c in seen:
                seen.remove(s[p1])
                p1 += 1
            seen.add(c)
            p2 += 1
            res = max(res, p2 - p1)
            
        return res