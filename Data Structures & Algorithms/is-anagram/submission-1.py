class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letter_dict = {}
        for letter in s:
            if letter not in s_letter_dict:
                s_letter_dict[letter] = 1
            else:
                s_letter_dict[letter] = s_letter_dict[letter] + 1
        t_letter_dict = {}
        for letter in t:
            if letter not in t_letter_dict:
                t_letter_dict[letter] = 1
            else:
                t_letter_dict[letter] = t_letter_dict[letter] + 1
        
        if s_letter_dict == t_letter_dict:
            return True
        return False