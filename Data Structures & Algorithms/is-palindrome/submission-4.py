class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnumStr = ""
        for currChar in s:
            if currChar.isalnum():
                alnumStr += currChar.lower()
            
        return alnumStr == alnumStr[::-1]