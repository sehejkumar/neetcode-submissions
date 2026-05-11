class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCounter = [0] *26
        for currLetter in s:
            charCounter[ord(currLetter) - ord('a')] += 1
        
        for currLetter in t:
            charCounter[ord(currLetter) - ord('a')] -= 1
        
        for i in range(26):
            if charCounter[i] != 0:
                return False
        
        return True

