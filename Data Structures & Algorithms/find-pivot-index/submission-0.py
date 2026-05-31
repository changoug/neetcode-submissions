class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # 1:21
        n = len(nums)
        left = [0] * (n + 1)
        right = [0] * (n + 1)

        for i in range(n):
            j = n - i - 1
            left[i] = nums[i] + left[i - 1]
            right[j] = nums[j] + right[j + 1]

        print(left)
        print(right)
        
        for i in range(n):
            if left[i] == right[i]:
                return i

        return -1
            