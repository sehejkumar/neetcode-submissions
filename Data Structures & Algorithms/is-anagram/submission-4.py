class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0] * 26
        for currLetter in s:
            freq[ord(currLetter) - ord('a')] += 1

        for currLetter in t:
            freq[ord(currLetter) - ord('a')] -= 1

        for i in range(26):
            if freq[i] != 0:
                return False

        return True