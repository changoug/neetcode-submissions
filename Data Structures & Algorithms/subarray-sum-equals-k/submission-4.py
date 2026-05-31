class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        pre = {0 : 1}
        res = curr = 0

        for n in nums:
            curr += n
            diff = curr - k

            res += pre.get(diff, 0)
            pre[curr] = 1 + pre.get(curr, 0)

        return res