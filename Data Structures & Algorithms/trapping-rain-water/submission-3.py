class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        L = 0
        R = len(height) - 1
        max_left = 0
        max_right = 0

        while L < R:
            if height[L] < height[R]:
                max_left = max(max_left, height[L])
                res += max_left - height[L]
                L += 1
            else:
                max_right = max(max_right, height[R])
                res += max_right - height[R]
                R -= 1
    
        return res