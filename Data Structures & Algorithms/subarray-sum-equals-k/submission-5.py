from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        pre = defaultdict(int)
        pre[0] = 1
        res = curr = 0

        for n in nums:
            curr += n
            diff = curr - k

            res += pre[diff]
            pre[curr] += 1

        return res