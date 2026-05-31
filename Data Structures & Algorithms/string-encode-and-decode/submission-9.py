class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for i in strs:
            res += i + "\n"
        return res

    def decode(self, s: str) -> List[str]:
        res = s.split("\n")
        return res[:-1]
