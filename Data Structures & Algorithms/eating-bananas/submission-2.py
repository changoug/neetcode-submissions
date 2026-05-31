class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1

        while low <= high:
            k = (high + low) // 2
            res = self.eat(piles, k)
            if res <= h:
                if k == 1 or self.eat(piles, k - 1) > h:
                    return k
                high = k - 1
            else:
                low = k + 1
        
        return k

    
    def eat(self, piles: List[int], k: int) -> int:
        t = 0

        for p in piles:
            t += (p // k)
            if (k > p) or (k % p) != 0:
                t += 1
            print(k, p, t)
        
        return t
