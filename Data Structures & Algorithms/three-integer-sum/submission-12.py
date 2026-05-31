class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for x in range(0, len(nums) - 1):
            
            if nums[x] > 0:
                break

            if x > 0 and nums[x] == nums[x - 1]:
                continue

            l = x + 1
            h = len(nums) - 1

            while l < h:
                s = nums[x] + nums[l] + nums[h]
                if s > 0:
                    h -= 1
                elif s < 0:
                    l += 1      
                else:
                    res.append([nums[x], nums[l], nums[h]])
                    l += 1
                    h -= 1
                    while nums[l] == nums[l - 1] and l < h:
                        l += 1
        return res
                