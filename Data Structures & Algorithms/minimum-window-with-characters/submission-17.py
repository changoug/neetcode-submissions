class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        count_t = Counter(t)
        freq = defaultdict(int)

        need = len(count_t)
        have = 0
        L = 0
        res = [0, 0]
        curr_min = 1000

        for R in range(len(s)):
            c = s[R]
            freq[c] += 1

            if c in count_t and freq[c] == count_t[c]:
                    have += 1

            while have == need:
                if curr_min > R - L + 1:
                    curr_min = R - L + 1
                    res = [L, R + 1]

                freq[s[L]] -= 1

                if s[L] in count_t and freq[s[L]] < count_t[s[L]]:
                    have -= 1

                L += 1

        return s[res[0]: res[1]]
