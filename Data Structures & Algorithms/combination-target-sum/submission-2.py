class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()

        def helper(tot: int, acc: List[int], nums: List[int], target) -> None:
            if tot == target:
                res.add(tuple(sorted(acc)))
            
            elif tot > target:
                return None

            else:
                for i in nums:
                    helper(tot + i, acc + [i], nums, target)

        for i in nums:
            helper(i, [i], nums, target)

        return [list(i) for i in res]
            
        


            

