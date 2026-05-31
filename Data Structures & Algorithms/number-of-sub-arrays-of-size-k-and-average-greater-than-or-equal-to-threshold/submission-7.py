class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr = sum(arr[:k])
        res = int(curr >= threshold * k)

        for R in range(k, len(arr)):
            curr = curr + arr[R] - arr[R - k]
            res += curr >= threshold * k
        
        return res