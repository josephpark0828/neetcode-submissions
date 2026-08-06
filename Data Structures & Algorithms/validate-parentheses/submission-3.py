class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(', '}':'{', ']':'['}
        stack = []

        for char in s:
            if stack and char in pairs.keys() and pairs[char] == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
            
        if not stack:
            return True
        return False