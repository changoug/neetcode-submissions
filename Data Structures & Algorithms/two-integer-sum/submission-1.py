class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums) - 1, -1, -1):
            if target - nums[i] not in d:
                d[nums[i]] = i
            else:
                return [i, d[target - nums[i]]]