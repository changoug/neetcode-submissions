class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        suf = [1] * n

        for i in range(1, n):
            pre[i] = nums[i - 1] * pre[i - 1]
            j = n - i - 1
            suf[j] = nums[j + 1] * suf[j + 1]

        return [pre[i] * suf[i] for i in range(n)]
