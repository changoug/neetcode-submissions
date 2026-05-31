from math import floor

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        mid = floor((low + high)/2)

        while low <= high:
            print(mid)
            if nums[mid] < target:
                low = mid + 1
                mid = floor((low + high)/2)
            
            elif nums[mid] > target:
                high = mid - 1
                mid = floor((low + high)/2)
            
            else:
                return mid

        return -1
