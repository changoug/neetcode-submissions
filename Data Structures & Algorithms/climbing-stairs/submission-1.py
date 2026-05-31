class Solution:
    def climbStairs(self, n: int) -> int:
        d = {0: 0, 1: 1, 2: 2}

        for i in range(2, n + 1):
            if i not in d:
                d[i] = d[i - 1] + d[i - 2]
    
        return d[n]

        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2

        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)

