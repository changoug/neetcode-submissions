class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        
        for n in num_set:
            if n - 1 not in num_set:
                curr_max = 1
                curr = n + 1
                while curr in num_set:
                    curr += 1
                    curr_max += 1
                res = max(res, curr_max)
        
        return res