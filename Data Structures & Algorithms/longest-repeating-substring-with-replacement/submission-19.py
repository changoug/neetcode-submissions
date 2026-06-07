class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = defaultdict(int)
        res = 0
        p = 0

        for i in range(len(s)):
            freq[s[i]] += 1
            if i - p + 1 - max(freq.values()) > k:
                freq[s[p]] -= 1
                p += 1

            res = max(res, i - p + 1)
            print(res, s[i])
        return res