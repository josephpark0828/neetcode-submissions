class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = {}
        counts_t = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            counts_s[s[i]] = counts_s.get(s[i], 0) + 1
            counts_t[t[i]] = counts_t.get(t[i], 0) + 1
        
        if counts_s == counts_t:
            return True
        return False