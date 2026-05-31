class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        res = 10 ** 6 + 1
        L = R = 0
        curr = 0

        while R < len(nums) or (curr >= target and L < len(nums)):
            if curr < target:
                curr += nums[R]
                R += 1
            else:
                res = min(res, R - L)
                curr -= nums[L]
                L += 1

        return res if res < 10 ** 6 + 1 else 0