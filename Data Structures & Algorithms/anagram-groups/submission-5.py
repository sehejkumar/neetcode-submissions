class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaMap = defaultdict(list)

        for currWord in strs:
            freqMap = [0] * 26
            for currChar in currWord:
                freqMap[ord(currChar) - ord('a')] +=1
            
            anaMap[tuple(freqMap)].append(currWord)

        return list(anaMap.values())