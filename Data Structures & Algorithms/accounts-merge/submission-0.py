class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        e_to_a = {}
        parent = [i for i in range(len(accounts))]
        rank = [0] * len(accounts)
        
        def find_parent(u):
            p = parent[u]

            while parent[p] != p:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        for i in range(len(accounts)):
            for e in accounts[i][1:]:
                if e in e_to_a:
                    p1 = find_parent(e_to_a[e])
                    p2 = find_parent(i)

                    if rank[p1] > rank[p2]:
                        e_to_a[e] = p1
                        parent[p2] = p1
                        rank[p1] += 1
                    else:
                        e_to_a[e] = p2
                        parent[p1] = p2
                        rank[p2] += 1

                else:
                    e_to_a[e] = find_parent(i)
        
        d = {}

        for i in range(len(accounts)):
            p = find_parent(i)
            if p not in d:
                d[p] = set()
            d[p].update(accounts[i][1:])
        
        res = []
        for p in d:
            res.append([accounts[p][0]] + sorted(d[p]))
        
        return res
