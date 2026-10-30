class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = [0] * 26
        l = 0
        r = 0
        res = 0
        mostFreq = 0

        for r in range(len(s)):
            mapIndex = ord(s[r]) - ord('A')
            freqMap[mapIndex] += 1
            mostFreq = max(mostFreq,freqMap[mapIndex])

            while (r-l+1) - mostFreq > k:
                freqMap[ord(s[l]) - ord('A')] -= 1
                l+=1

            res = max(res, r-l+1)
        return res
            
            




        