class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.lru = {}
        self.capacity = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, key, val) -> None:
        node = Node(key, val)
        self.right.prev.next = node
        node.prev = self.right.prev
        self.right.prev = node
        node.next = self.right

    def remove(self, key) -> None:
        node = self.lru[key]
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.lru:
            self.remove(key)
            self.insert(key, self.lru[key].val)
            self.lru[key] = self.right.prev
            return self.right.prev.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.remove(key)
        self.insert(key, value)
        self.lru[key] = self.right.prev

        if len(self.lru) > self.capacity:
            node = self.left.next
            self.remove(node.key)
            del self.lru[node.key]
            
