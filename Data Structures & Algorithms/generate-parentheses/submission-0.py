class Solution:
    def generateParenthesis(self, n):
        res = []
        for i in range(n + 1):
            res.append([])

        res[0] = [""]
        
        for k in range(n + 1):
            for i in range(k):
                for left in res[i]:
                    for right in res[k-i-1]:
                        res[k].append("(" + left + ")" + right)
        
        return res[-1]