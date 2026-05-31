class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        signal = -1
        cnt = 0
        res = 0

        for i in range(1, len(arr)):
            if arr[i - 1] < arr[i]:
                cnt = cnt + 1 if signal == 0 else 1
                signal = 1
            
            elif arr[i - 1] > arr[i]:
                cnt = cnt + 1 if signal == 1 else 1
                signal = 0
            
            else:
                cnt = 0
                signal = -1

            res = max(cnt, res)

        return res + 1