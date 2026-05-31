class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 2:12
        n = len(nums)
        res = [1] * n
        right = 1

        for i in range(n - 1):
            res[i + 1] = nums[i] * res[i]

        for i in range(n - 1, 0, -1):
            right = nums[i] * right
            res[i - 1] *= right

        return res