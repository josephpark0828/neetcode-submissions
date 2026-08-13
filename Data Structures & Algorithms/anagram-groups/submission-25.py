class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        anagrams = {}
        
        for s in strs:
            if "".join(sorted(s)) in anagrams.keys():
                anagrams["".join(sorted(s))].append(s)
            else:
                anagrams["".join(sorted(s))] = [s]

        for array in anagrams.values():
            groups.append(array)
        
        return groups