class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        res = 0
        L = 0
        curr = 0

        for R in range(len(arr)):
            curr += arr[R]
            if R - L + 1 == k:
                res += curr >= threshold * k
                curr -= arr[L]
                L += 1
        
        return res