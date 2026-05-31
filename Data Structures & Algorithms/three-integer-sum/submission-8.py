class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = {}
        res = []
        seen = set()

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] not in d:
                    d[nums[i] + nums[j]] = []
                d[nums[i] + nums[j]].append(tuple((nums[i], nums[j], i, j)))
        
        for x in range(len(nums)):
            if -nums[x] not in d:
                continue

            for y in d[-nums[x]]:
                n_i, n_j, i, j = y
                if x == i or x == j:
                    continue
                r = sorted([n_i, n_j, nums[x]])
                if tuple(r) not in seen:
                    res.append(r)
                    seen.add(tuple(r))
        
        return res
                