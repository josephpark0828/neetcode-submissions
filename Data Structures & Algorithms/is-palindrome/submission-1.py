class Solution:
    def isPalindrome(self, s: str) -> bool:
        # change to lowercase
        lower_s = s.lower()

        # remove spaces
        formatted_s = ''
        for char in lower_s:
            if char.isalnum():
                formatted_s += char

        # check if s == reversed s
        if formatted_s == formatted_s[::-1]:
            return True
        return False