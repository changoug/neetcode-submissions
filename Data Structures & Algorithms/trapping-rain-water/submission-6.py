class Solution:
    def trap(self, height: List[int]) -> int:

        res = 0

        pre_max = 0
        suf_max = 0

        hl = len(height)

        pre_lst = [0] * hl
        suf_lst = [0] * hl

        for i in range(hl):

            pre_max = max(pre_max, height[i])
            suf_max = max(suf_max, height[hl - i - 1])
            pre_lst[i] = pre_max
            suf_lst[hl - i - 1] = suf_max

        for i in range(hl):
            res += min(pre_lst[i], suf_lst[i]) - height[i]
        
        return res
