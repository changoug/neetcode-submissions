class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        prev = [0] * n

        for r in range(m - 1, -1 , -1):
            curr = [0] * n
            if obstacleGrid[r][n - 1] == 0 and (obstacleGrid[r][n - 2] == 0 or obstacleGrid[r - 1][n - 1] == 0):
                curr[n - 1] = 1 if r == m - 1 else prev[n - 1]

            for c in range(n - 2, -1, -1):
                if obstacleGrid[r][c] == 0:
                    curr[c] = curr[c + 1] + prev[c]

            print(curr)
            prev = curr
    
        return prev[0]