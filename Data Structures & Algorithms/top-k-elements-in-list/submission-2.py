from collections import Counter
from heapq import heapify, heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        h = []
        heapify(h)

        count = Counter(nums)

        for c in count:
            heappush(h, (-int(count[c]), c))
        
        return [int(heappop(h)[1]) for _ in range(k)]