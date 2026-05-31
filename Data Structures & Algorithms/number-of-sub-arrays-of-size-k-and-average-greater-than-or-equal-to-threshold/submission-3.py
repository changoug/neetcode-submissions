class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        res = 0
        L = 0
        curr = sum(arr[:k - 1])

        for R in range(k - 1, len(arr)):
            curr += arr[R]
            res += curr >= threshold * k
            curr -= arr[L]
            L += 1
        
        return res