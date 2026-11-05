class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaMap = defaultdict(list)

        for s in strs:
            freqMap = [0] * 26
            for currChar in s:
                freqMap[ord(currChar) - ord('a')] +=1
            key = tuple(freqMap)
            anaMap[key].append(s)

        return list(anaMap.values())