class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        t_count = Counter(t)
        freq = defaultdict(int)

        L = 0
        res = [0, 0]
        curr_min = len(s) + 1
        have = 0
        need = len(t_count)

        for R in range(len(s)):
            freq[s[R]] += 1

            if s[R] in t_count and freq[s[R]] == t_count[s[R]]:
                have += 1

            while have == need:
                if curr_min > R - L + 1:
                    curr_min = R - L + 1
                    res = [L, R + 1]

                freq[s[L]] -= 1
                if s[L] in t_count and freq[s[L]] < t_count[s[L]]:
                    have -= 1
                L += 1

        return s[res[0]: res[1]]
