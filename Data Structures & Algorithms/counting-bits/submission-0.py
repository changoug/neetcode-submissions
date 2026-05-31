class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n + 1):
            acc = 0
            while i != 0:
                if i % 2 != 0:
                    acc += 1
                i = i >> 1
            
            res.append(acc)

        return res