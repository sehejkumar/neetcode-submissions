class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqMap = [0]*26
        for currChar in s:
            freqMap[ord(currChar) - ord('a')] +=1
        
        for currChar in t:
            freqMap[ord(currChar) - ord('a')] -=1

        for i in range(26):
            if freqMap[i] != 0:
                return False

        return True