class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1
        
        k_max = []

        for _ in range(k):
            n = max(freq, key=freq.get)
            k_max.append(n)
            del freq[n]
        
        return k_max
