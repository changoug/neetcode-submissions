class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        n = len(nums)

        while True:
            slow = (slow + 1) % n
            fast = (fast + 2) % n
            if nums[slow] == nums[fast]:
                return nums[slow]