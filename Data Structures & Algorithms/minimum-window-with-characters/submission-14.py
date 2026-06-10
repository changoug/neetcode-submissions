class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        count_t = Counter(t)
        freq = defaultdict(int)

        need = len(t)
        have = 0

        L = 0
        res = [0, 1000]

        for R in range(len(s)):
            c = s[R]

            if c in count_t and freq[c] < count_t[c]:
                    have += 1
            
            freq[c] += 1
                

            while have == need:
                if res[1] - res[0] > R - L:
                    res = [L, R]

                freq[s[L]] -= 1

                if freq[s[L]] < count_t[s[L]]:
                    have -= 1

                L += 1

            print(c, have, need, L, R, res, freq)
        
        print(res[1] - res[0])

        return s[res[0]: res[1] + 1] if res[1] - res[0] < 1000 else ""
