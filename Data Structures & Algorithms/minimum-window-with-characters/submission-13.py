class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        t_count = Counter(t)
        freq = defaultdict(int)

        L = 0
        res = [0, 0]
        curr_min = len(s) + 1

        for R in range(len(s)):
            freq[s[R]] += 1

            while all(freq[k] >= t_count[k] for k in t_count):
                if curr_min > R - L + 1:
                    curr_min = R - L + 1
                    res = [L, R + 1]
                freq[s[L]] -= 1
                L += 1

        return s[res[0]: res[1]]