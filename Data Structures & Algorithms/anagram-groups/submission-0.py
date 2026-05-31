class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}
        for s in strs:
            s_sorted = ''.join(sorted(s))
            if s_sorted not in ana:
                ana[s_sorted] = []

            ana[s_sorted].append(s)
        return ana.values()