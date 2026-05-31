import heapq

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.heap = []
        self.item_id = 0
        
    def pop(self, key: int) -> int:
        temp = []
        res = -1

        while self.heap and (not temp or temp[-1][1] != key):
            temp.append(heapq.heappop(self.heap))

        if temp and temp[-1][1] == key:
            res = temp.pop()[2]

        for i in temp:
            heapq.heappush(self.heap, i)
        return res

    def get(self, key: int) -> int:
        res = self.pop(key)
        if res != -1:
            heapq.heappush(self.heap, (self.item_id, key, res))
            self.item_id += 1
        return res

    def put(self, key: int, value: int) -> None:
        self.pop(key)
        heapq.heappush(self.heap, (self.item_id, key, value))
        self.item_id += 1

        if len(self.heap) > self.capacity:
            heapq.heappop(self.heap)

        
