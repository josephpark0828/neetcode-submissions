class Solution:

    def encode(self, strs: List[str]) -> str:
        single_str = []
        
        for word in strs:
            for char in word:
                single_str.append(char)
            single_str.append('.')

        formatted_single_str = ''.join(single_str)
        
        return formatted_single_str

    def decode(self, s: str) -> List[str]:
        res = []

        temp = []
        formatted_temp = []
        for char in s:
            if char != '.':
                temp.append(char)
            else:
                formatted_temp = ''.join(temp)
                res.append(formatted_temp)
                temp = []
                formatted_temp = []

        return res