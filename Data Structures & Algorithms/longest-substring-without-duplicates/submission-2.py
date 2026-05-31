class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        res = 0
        L = R = 0
        while R < len(s):
            if s[R] in hash_set:
                hash_set.remove(s[L])
                L += 1
            else:
                hash_set.add(s[R])
                R += 1
                res = max(res, R - L)
        return res