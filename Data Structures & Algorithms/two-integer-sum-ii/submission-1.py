from bisect import bisect_right

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(numbers)):
            if numbers[i] in d:
                return [d[numbers[i]] + 1, i + 1]
            d[target - numbers[i]] = i
            