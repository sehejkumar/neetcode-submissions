class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqMap = [0] * 26

        for currLetter in s:
            freqMap[ord(currLetter) - ord('a')] +=1

        for currLetter in t:
            freqMap[ord(currLetter) - ord('a')] -=1
        
        for i in range(26):
            if freqMap[i] != 0:
                return False
        return True
            