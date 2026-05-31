class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        curr = [0] * (len(text2) + 1)
        prev = [0] * (len(text2) + 1)

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    curr[j] = prev[j + 1] + 1
                else:
                    curr[j] = max(curr[j + 1], prev[j])
            prev = curr[:]

        return curr[0]