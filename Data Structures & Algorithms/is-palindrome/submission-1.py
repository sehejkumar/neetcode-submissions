class Solution:
    def isPalindrome(self, s: str) -> bool:
        # alphaNumString = "".join(currChar for currChar in s if currChar.isalnum())
        # alphaNumString = alphaNumString.lower()
        # i = 0
        # j = len(alphaNumString) - 1
        # while (i < j):
        #     if alphaNumString[i] != alphaNumString[j]:
        #         return False
        #     i+=1
        #     j-=1

        # return True

        alphaNumStr = ''
        for currChar in s:
            if currChar.isalnum():
                alphaNumStr += currChar.lower()
        return alphaNumStr == alphaNumStr[::-1]

        