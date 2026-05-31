class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            curr = str(sorted(s))
            if curr not in d:
                d[curr] = []
            d[curr].append(s)
        return [d[i] for i in d]