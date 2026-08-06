class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initialize left and right pointers
        l = 0
        r = len(s) - 1

        # move each pointer towards center and check if each letter is the same
        while l < r:
            while l < r and not self.alphanumeric(s[l]):
                l += 1
            while r > l and not self.alphanumeric(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def alphanumeric(self, c):
        return(ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))