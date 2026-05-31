class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        res = 0
        L = 0
        curr = 0

        for R in range(len(arr)):
            curr += arr[R]

            if R - L + 1 == k:
                if curr / k >= threshold:
                    res += 1
                curr -= arr[L]
                L += 1
        
        return res