class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # stores (index, temperature)
        res = [0] * len(temperatures)

        for currIndex, currTemp in enumerate(temperatures):
            # compare with the TOP of the stack
            #if today hotter than previous
            while stack and stack[-1][1] < currTemp:
                #remove previous day
                stackIndex, stackTemp = stack.pop()
                #calculate num days
                res[stackIndex] = currIndex - stackIndex
            #add today
            stack.append((currIndex, currTemp))

        return res