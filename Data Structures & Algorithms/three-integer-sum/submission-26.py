class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = set()

        for i in range(1, len(nums) - 1):
            l = 0
            r = len(nums) - 1
            while l < r and l != i and r != i:
                if nums[l] + nums[r] + nums[i] == 0:
                    res.add((nums[l], nums[i], nums[r]))
                    l += 1
                    r -= 1
                
                elif nums[l] + nums[r] + nums[i] < 0:
                    l += 1
                
                else:
                    r -= 1

        return [[l, i, r] for l, i, r in res]
            
            