class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsdict = defaultdict(list)
        
        for word in strs:
            sortedword = sorted(word)
            formattedword = ''.join(sortedword)
            anagramsdict[formattedword].append(word)
        
        return list(anagramsdict.values())