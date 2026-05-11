class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i] = 1
        for j in t:
            if j in freq:
                freq[j] -= 1
            else:
                freq[j] = 1
        for letter in freq:
            if freq[letter] != 0:
                return False
        return True  