class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res = res + word + '.'
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        word = ''
        for char in s:
            if char == '.':
                res.append(word)
                word = ''
            else:
                word = word + char
        
        return res