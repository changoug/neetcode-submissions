class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        h = len(numbers) - 1

        while l < h:
            curr = numbers[l] + numbers[h]

            if curr > target:
                h -= 1
            elif curr < target:
                l += 1
            else:
                return [l + 1, h + 1]
            
            