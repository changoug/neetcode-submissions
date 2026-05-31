class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        discovered = set()

        # for i in nums:
        #     discovered.add(tuple([i]))
        
        discovered.add(tuple(nums))
        discovered.add(tuple([]))
        
        def dfs(sub: List[int]) -> None:
            for i, v in enumerate(sub):
                to_add = tuple(sub[:i] + sub[i + 1:])
                if to_add not in discovered:
                    discovered.add(to_add)
                    dfs(to_add)

        dfs(nums)

        return [list(i) for i in discovered]