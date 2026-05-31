import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = []
        for i in s:
            if i.isalnum():
                l.append(i.lower())
        sanitized_s = ''.join(l)
        return sanitized_s == sanitized_s[::-1]