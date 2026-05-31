class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent = [i for i in range(n)]
        rank = [0] * n
        res = n

        def find_parent(i):
            p = i
            while parent[p] != p:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        for a, b in edges:
            n1 = find_parent(a)
            n2 = find_parent(b)

            if n1 == n2:
                continue
            res -= 1

            if rank[n1] > rank[n2]:
                rank[n1] += 1
                parent[n2] = n1
            
            else:
                rank[n2] += 1
                parent[n1] = n2


        return res