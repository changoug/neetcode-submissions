class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([i + "\n" for i in strs])

    def decode(self, s: str) -> List[str]:
        return s.split("\n")[:-1]
