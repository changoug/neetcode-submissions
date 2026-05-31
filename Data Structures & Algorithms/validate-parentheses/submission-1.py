class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        open_brack = {'(', '{', '['}
        brack_dict = {')': '(', '}': '{', ']': '['}

        for i in s:
            if i in open_brack:
                stack.append(i)
            else:
                if stack == []:
                    return False
                top = stack.pop()
                if top != brack_dict[i]:
                    return False
        return stack == []


