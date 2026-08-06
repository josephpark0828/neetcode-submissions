class Solution:
    def isPalindrome(self, s: str) -> bool:
        # make it all lowercase and get rid of the spaces
        string = ''
        for char in s:
            if char.isalnum():
                string += char.lower()
        print(string)

        # have a pointer at each end and compare each letter and make your way to the middle
        i = 0
        j = len(string)

        while i < j:
            start = string[i]
            end = string[j - 1]
            if start != end:
                return False
            i += 1
            j -= 1
        
        return True