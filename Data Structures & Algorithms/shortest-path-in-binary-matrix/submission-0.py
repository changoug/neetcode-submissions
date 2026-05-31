from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        visited = set()
        q = deque([(0, 0)])
        n = len(grid)
        length = 0
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

        while q:
            lvl = []
            length += 1

            for _ in range(len(q)):
                lvl.append(q.popleft())

            for r, c in lvl:

                if min(r, c) < 0 or max(r, c) >= n or (r, c) in visited or grid[r][c] == 1:
                    continue

                if r == n - 1 and c == n - 1:
                    return length

                visited.add((r, c))

                for dr, dc in neighbors:
                    q.append((r + dr, c + dc))
        
        return -1
            


                
            