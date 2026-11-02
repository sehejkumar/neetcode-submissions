class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []

        for currBracket in s:
            if currBracket in bracketMap:
                if not stack: 
                    return False
                top = stack.pop()
                if bracketMap[currBracket] != top:
                    return False
            else:
                stack.append(currBracket)

        if stack: 
            return False
        else: 
            return True
