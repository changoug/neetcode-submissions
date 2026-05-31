class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        if strs == []:
            return s
            
        for i in strs:
            s += (str(len(i)) + '-' + i)
        return s

    def decode(self, s: str) -> List[str]:
        lst = []
        i = 0
        word_length = ''

        while i < len(s):
            if s[i].isnumeric():
                word_length += s[i]
                i += 1
            elif s[i] == '-':
                word_length = int(word_length)
                i += 1
                lst.append(s[i: i + word_length])
                i += word_length
                word_length = ''
        return lst
            



