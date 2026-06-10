class Solution:
    def isValid(self, s: str) -> bool:

        b = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:

            if c in b:
                stack.append(c)

            elif not stack or b[stack.pop()] != c:
                return False
        
        return not stack
