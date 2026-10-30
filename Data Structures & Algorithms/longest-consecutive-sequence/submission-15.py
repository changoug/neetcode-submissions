class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set(nums)
        res = 0

        for n in s:
            if n - 1 not in s:
                curr = 1
                while n + curr in s:
                    curr += 1
            
                res = max(res, curr)

        return res
                