class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:
            curr = [0] * 26
            for c in s:
                curr[ord(c) - 100] += 1

            res[str(curr)].append(s)
        
        return list(res.values())
