class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        i = len(matrix) - 1

        while matrix[i][0] > target and i > 0:
            i -= 1
        
        return self.binarySearch(matrix[i], target)




    def binarySearch(self, nums: List[int], target: int) -> bool:
        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2

        while low <= high:
            if nums[mid] < target:
                low = mid + 1
                mid = (low + high) // 2
            elif nums[mid] > target:
                high = mid - 1
                mid = (low + high) // 2
            else:
                return True
        
        return False
