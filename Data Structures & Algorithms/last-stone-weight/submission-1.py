import heapq        
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            if x > y:
                heapq.heappush(heap, y - x)
            
            elif x < y:
                heapq.heappush(heap, x - y)
        
        if heap:
            return -heap[0]
        
        return 0