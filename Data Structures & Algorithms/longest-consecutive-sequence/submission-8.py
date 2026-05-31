class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}

        for n in nums:
            d[n] = 1

        seen = set()
        
        for n in nums:
            if n - 1 not in d and n not in seen:
                seen.add(n)
                curr = n + 1
                while curr in d:
                    print(d[n], n)
                    d[n] += 1
                    curr += 1
        
        return max(d.values()) if nums != [] else 0