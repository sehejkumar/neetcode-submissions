class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # need to sort all the characters in the anagrams
        sortedAnagrams = defaultdict(list)
        for currStr in strs:
            sortedStr = "".join(sorted(currStr))
            sortedAnagrams[sortedStr].append(currStr)
        return list(sortedAnagrams.values())