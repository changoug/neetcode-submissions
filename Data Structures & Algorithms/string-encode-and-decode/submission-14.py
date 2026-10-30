class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            res.append(str(len(s)) + '#' + s)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        i = 0
        length = ""
        res = []

        while i < len(s):
            if s[i] != '#':
                length += s[i]
                i += 1
            else:
                i += 1
                res.append(s[i: i + int(length)])
                i += int(length)
                length = ""

        return res
