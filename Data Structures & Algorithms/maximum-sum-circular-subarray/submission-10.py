
from math import inf
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        glob_max = nums[0]
        glob_min = nums[0]
        curr_max = -inf
        curr_min = inf
        total = 0

        for n in nums:
            total += n
            curr_max = max(n, curr_max + n)
            curr_min = min(n, curr_min + n)

            glob_max = max(glob_max, curr_max)
            glob_min = min(glob_min, curr_min)

        return glob_max if glob_max > total - glob_min  or total < 0 else total - glob_min