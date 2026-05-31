from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        n_pre = defaultdict(list)
        visited = set()

        def dfs(node):
            if node not in n_pre:
                return True
            
            elif node in visited and node in n_pre:
                return False
            
            visited.add(node)
            for n in n_pre[node]:
                if not dfs(n):
                    return False
            
            visited.remove(node)
            return True

        for n1, n2 in prerequisites:
            n_pre[n1].append(n2)
        
        for n1, n2 in prerequisites:
            if not dfs(n1):
                return False
        
        return True


        
        