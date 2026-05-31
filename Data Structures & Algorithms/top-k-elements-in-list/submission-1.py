class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        return sorted(list(c), key=lambda x: c[x], reverse=True)[:k]