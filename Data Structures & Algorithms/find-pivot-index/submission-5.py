class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # 1:21
        n = len(nums)
        total = sum(nums)
        left = 0

        for i in range(n):
            left = nums[i] + left
            right = total - left
            if left - nums[i] == right:
                return i

        return -1
            