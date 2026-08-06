class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = []
        t_letters = []

        for i in range(len(s)):
            s_letters.append(s[i])
        
        for i in range(len(t)):
            t_letters.append(t[i])
        
        if sorted(s_letters) == sorted(t_letters):
            return True
        return False