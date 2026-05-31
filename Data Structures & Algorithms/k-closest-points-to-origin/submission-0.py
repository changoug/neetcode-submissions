import heapq  
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []

        for p in points:
            x = p[0]
            y = p[1]

            d = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(h, (d, x, y))

        res = []

        while k > 0 and h:
            _, x, y = heapq.heappop(h)
            res.append([x, y])
            k -= 1

        return res