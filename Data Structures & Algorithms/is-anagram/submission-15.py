class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_counts = defaultdict(int)
        t_counts = defaultdict(int)

        for i in range(len(s)):
            s_counts[s[i]] = s_counts.get(0, s_counts[s[i]]) + 1
            t_counts[t[i]] = t_counts.get(0, t_counts[t[i]]) + 1
    
        print(s_counts)
        
        if s_counts == t_counts:
            return True
        
        return False