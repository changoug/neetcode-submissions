class Node:

    def __init__(self, val: int, key: int) -> None:
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.capacity = capacity
        self.first = None
        self.last = None

    def pop(self, key: int) -> int:
        if key not in self.d:
            return -1
        
        node = self.d[key]
        del self.d[key]

        if node.prev:
            node.prev.next = node.next
        
        if node.next:
            node.next.prev = node.prev

        if self.first == node:
            self.first = self.first.next
        
        if self.last == node:
            self.last = self.last.prev
        
        return node.val


    def get(self, key: int) -> int:
        val = self.pop(key)
        if val == -1:
            return val

        new_node = Node(val, key)
        self.d[key] = new_node

        if self.first is None:
            self.first = new_node
            self.last = new_node
        
        elif self.first == self.last:
            self.first.next = new_node
            new_node.prev = self.first
            self.last = new_node
        
        else:
            self.last.next = new_node
            new_node.prev = self.last
            self.last = self.last.next
        
        return val

    def put(self, key: int, value: int) -> None:
        self.pop(key)
        new_node = Node(value, key)
        self.d[key] = new_node

        if self.first is None:
            self.first = new_node
            self.last = new_node
        
        elif self.first == self.last:
            self.first.next = new_node
            new_node.prev = self.first
            self.last = new_node
        
        else:
            self.last.next = new_node
            new_node.prev = self.last
            self.last = self.last.next
        
        if len(self.d) > self.capacity:
            to_del = self.first.key
            self.first = self.first.next
            self.first.prev = None
            del self.d[to_del]




        
