class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaMap = defaultdict(list)
        for currStr in strs:
            freqMap = [0] * 26
            for currChar in currStr:
                freqMap[ord(currChar) - ord('a')] +=1
            key = tuple(freqMap)
            anaMap[key].append(currStr)
        return list(anaMap.values())