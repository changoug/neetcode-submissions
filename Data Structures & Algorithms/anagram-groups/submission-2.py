class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:
            curr = str(sorted(s))
            res[curr].append(s)
        
        return list(res.values())
