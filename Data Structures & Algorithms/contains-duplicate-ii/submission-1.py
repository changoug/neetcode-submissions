class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        L = 0
        for R in range(len(nums)):
            if nums[R] in s:
                return True
            
            s.add(nums[R])
            
            if len(s) > k:
                s.remove(nums[L])
                L += 1

        return False