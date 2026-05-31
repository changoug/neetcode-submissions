import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = [-i for i in nums]
        self.k = k
        heapq.heapify(self.h)

    def add(self, val: int) -> int:
        heapq.heappush(self.h, -val)
        temp = []
        for _ in range(self.k):
            temp.append(heapq.heappop(self.h))
        
        res = -temp[-1]

        for i in temp:
            heapq.heappush(self.h, i)
        
        return res