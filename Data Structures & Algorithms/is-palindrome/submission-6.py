class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = "".join([c for c in s if c.isalnum()]).lower()
        return l == l[::-1]
