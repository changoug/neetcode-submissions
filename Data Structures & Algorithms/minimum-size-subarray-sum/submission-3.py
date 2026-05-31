class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        res = 10 ** 6 + 1
        L = R = 0
        curr = 0

        while R < len(nums):
            if curr < target:
                curr += nums[R]
                R += 1
            else:
                res = min(res, R - L)
                curr -= nums[L]
                L += 1
        
        while curr >= target and L < len(nums):
            res = min(res, R - L)
            curr -= nums[L]
            L += 1


        return res if res < 10 ** 6 + 1 else 0