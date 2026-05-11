class Solution:
    def isValid(self, s: str) -> bool:
        #we need to map the correct parenthesis so hashmap
        bracketMap = {")": "(", "]": "[", "}": "{"}
        stack = []
        for currBracket in s:
            if currBracket in bracketMap:
                if stack and stack[-1] == bracketMap[currBracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(currBracket)
        return True if not stack else False