class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        dp = [[0, 0] for i in range(len(arr) + 1)]
        res = 0
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] > arr[i - 1]:
                dp[i][0] = dp[i + 1][1] + 1
            
            elif arr[i] < arr[i - 1]:
                dp[i][1] = dp[i + 1][0] + 1
            res = max(res, dp[i][0], dp[i][1])

        return res + 1