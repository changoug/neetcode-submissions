class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        curr = [0] * (len(text2) + 1)

        for i in range(len(text1) - 1, -1, -1):
            prev = 0
            for j in range(len(text2) - 1, -1, -1):
                temp = curr[j]
                if text1[i] == text2[j]:
                    curr[j] = prev + 1
                else:
                    curr[j] = max(curr[j + 1], curr[j])
                prev = temp

        return curr[0]