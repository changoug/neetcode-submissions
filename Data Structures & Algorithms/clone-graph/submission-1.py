"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        q = deque()
        recreated = {}
        
        if node is not None:
            q.append(node)
            recreated[node] = Node(node.val)

        while q:
            curr = q.popleft()

            for n in curr.neighbors:
                if n not in recreated:
                    recreated[n] = Node(n.val)
                    q.append(n)

                recreated[curr].neighbors.append(recreated[n])

                
        if node:
            return recreated[node]
        
        return None


