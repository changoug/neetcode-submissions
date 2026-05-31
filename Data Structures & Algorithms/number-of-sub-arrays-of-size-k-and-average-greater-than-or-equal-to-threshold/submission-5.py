class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        curr = sum(arr[:k])
        res = int(curr >= threshold * k)

        for R in range(k, len(arr)):
            curr = curr + arr[R] - arr[L]
            L += 1
            res += curr >= threshold * k
        
        return res