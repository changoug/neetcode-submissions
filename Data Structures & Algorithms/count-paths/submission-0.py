class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1] * n

        for r in range(m - 2, -1, -1):
            curr = [0] * n
            curr[n - 1] = 1

            for c in range(n - 2, -1, -1):
                curr[c] = curr[c + 1] + prev[c]
            
            print(curr)

            prev = curr
        
        return prev[0]