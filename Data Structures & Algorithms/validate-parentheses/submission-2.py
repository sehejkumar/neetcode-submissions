class Solution:
    def isValid(self, s: str) -> bool:
        brackets={')': '(', ']': '[', '}': '{'}
        stack=[]
        for currBracket in s:
            if currBracket in brackets:
                if stack and stack[-1] == brackets[currBracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(currBracket)
        return True if not stack else False
