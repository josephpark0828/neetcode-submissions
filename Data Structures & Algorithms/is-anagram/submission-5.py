class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        for letter in s:
            if letter not in countS:
                countS[letter] = 1
            else:
                countS[letter] = countS[letter] + 1
        countT = {}
        for letter in t:
            if letter not in countT:
                countT[letter] = 1
            else:
                countT[letter] = countT[letter] + 1
        
        if countS == countT:
            return True
        return False