class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        res = min(heights[R], heights[L]) * R

        while L < R:
            res = max(res, min(heights[R], heights[L]) * (R - L))
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1

        return res