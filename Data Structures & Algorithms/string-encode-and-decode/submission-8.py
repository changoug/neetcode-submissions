class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for i in strs:
            res += i + "\changoug"
        return res

    def decode(self, s: str) -> List[str]:
        res = s.split("\changoug")
        return res[:-1]
