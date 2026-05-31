class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = defaultdict(int)

        L = 0
        curr_max = 0

        for R in range(len(s)):
            cnt[s[R]] += 1
            if cnt[s[R]] > curr_max:
                curr_max = cnt[s[R]]
            
            if R - L + 1 > curr_max + k:
                cnt[s[L]] -= 1
                L += 1

        return min(len(s), curr_max + k)