class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 2:12
        n = len(nums)
        left = [1] * (n + 1)
        right = [1] * (n + 1)

        for i in range(len(nums)):
            j = n - i - 1
            left[i + 1] = nums[i] * left[i]
            right[j - 1] = nums[j] * right[j]

        return [left[i] * right[i] for i in range(n)]