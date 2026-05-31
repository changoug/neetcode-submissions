class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        max_left = [0]
        max_right = [0]
        R = len(height) - 1
        for L in range(len(height)):
            max_left.append(max(max_left[-1], height[L]))
            max_right.append(max(max_right[-1], height[R]))
            R -= 1

        R = len(height) - 1
        for L in range(len(height)):
            res += max(min(max_left[L], max_right[R]) - height[L], 0)
            R -= 1

        print(max_left)
        max_right.reverse()
        print(max_right)
        return res