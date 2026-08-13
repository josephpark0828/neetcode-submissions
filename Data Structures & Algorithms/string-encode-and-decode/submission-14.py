class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        for word in strs:
            s += word
            s += "\n"

        return s

    def decode(self, s: str) -> List[str]:
        array = []
        word = []
        
        for char in s:
            if char != "\n":
                word.append(char)
            else:
                array.append("".join(word))
                word = []
        
        return array
        
