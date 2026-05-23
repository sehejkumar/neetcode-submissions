class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []
        newVal = 0
        for currToken in tokens:
            if currToken not in operators:
                stack.append(int(currToken))
            else:
                firstNum = stack.pop()
                secondNum = stack.pop()
                if currToken == '+':
                    newVal = firstNum + secondNum
                if currToken == '-':
                    newVal = secondNum - firstNum
                if currToken == '*':
                    newVal = firstNum * secondNum
                if currToken == '/':
                    newVal = int(secondNum/firstNum)
                stack.append(newVal)
        return stack[0]
