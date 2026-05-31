class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = [1] * len(nums)
        suf = [1] * len(nums)
        
        for i in range(len(nums) - 1):
            pre[i + 1] *= nums[i] * pre[i]

        for j in range(len(nums) - 1, 0, -1):
            suf[j - 1] *= nums[j] * suf[j]
        
        return [pre[i] * suf[i] for i in range(len(nums))]

