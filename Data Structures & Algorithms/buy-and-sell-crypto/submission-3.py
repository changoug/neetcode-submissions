class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        low = (100, 0)
        res = 0

        for i, p in enumerate(prices):
            low = min(low, (p, i))
            if low[1] < i and low[0] < p:
                res = max(res, p - low[0])
        
        return res