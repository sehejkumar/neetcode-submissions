class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenMap = {} #map to store last index of character
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in seenMap:
                l = max(seenMap[s[r]]+1, l)
            seenMap[s[r]] = r
            res = max(res, r - l + 1)
        return res