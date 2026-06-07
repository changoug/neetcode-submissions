class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        L = 0
        s1_count = Counter(s1)
        s2_count = defaultdict(int)

        for R in range(len(s2)):
            s2_count[s2[R]] += 1
            if R - L + 1 > len(s1):
                s2_count[s2[L]] -= 1
                if s2_count[s2[L]] == 0:
                    del s2_count[s2[L]]
                L += 1
            if s2_count == s1_count:
                return True
        return False


        