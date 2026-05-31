class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        parent = {}
        rank = {}

        for n in nums:
            parent[n] = n

        def find_parent(node):
            p = node
            while parent[p] != p:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        for i in nums:
            if i in rank:
                continue
            
            rank[i] = 1

            if i + 1 in rank:
                n1 = find_parent(i)
                n2 = find_parent(i + 1)

                if n1 != n2:
                    if rank[n1] > rank[n2]:
                        rank[n1] += rank[n2]
                        parent[n2] = n1
                    
                    else:
                        rank[n2] += rank[n1]
                        parent[n1] = n2

            if i - 1 in rank:
                n1 = find_parent(i)
                n3 = find_parent(i - 1)

                if n1 != n3:
                    if rank[n1] > rank[n3]:
                        rank[n1] += rank[n3]
                        parent[n3] = n1
                    
                    else:
                        rank[n3] += rank[n1]
                        parent[n1] = n3

        res = list(rank.values())
        res.append(0)

        return max(res)

