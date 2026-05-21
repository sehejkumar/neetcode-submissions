class Solution:
    def isValid(self, s: str) -> bool:
        validMap = {')': '(', ']':"[", '}': '{' }
        stack=[]
        for currChar in s:
            if currChar in validMap:
                if stack and stack[-1] == validMap[currChar]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(currChar)
        return True if not stack else False
