class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = "".join(char for char in s if char.isalnum()).lower()
        return res == res[::-1]