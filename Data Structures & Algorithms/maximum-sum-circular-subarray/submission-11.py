class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        glob_max = nums[0]
        glob_min = nums[0]
        curr_max = 0
        curr_min = 0
        total = 0

        for n in nums:
            curr_max = max(n, curr_max + n)
            curr_min = min(n, curr_min + n)
            total += n
            glob_max = max(glob_max, curr_max)
            glob_min = min(glob_min, curr_min)

        return max(glob_max, total - glob_min) if glob_max > 0 else glob_max