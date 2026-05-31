class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        L = curr_max = 0

        for R in range(len(s)):
            cnt[s[R]] += 1
            if R - L > curr_max + k:
                cnt[s[L]] -= 1
                L += 1
            curr_max = max(curr_max, cnt[s[R]])
        return min(len(s), curr_max + k)