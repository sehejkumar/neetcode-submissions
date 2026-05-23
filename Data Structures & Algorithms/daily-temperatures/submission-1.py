class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #return array of days until next is warmer
        res = [0] * len(temperatures)
        stack = [] #store index,temp
        for currIndex, currTemp in enumerate(temperatures):
            #while stack not empty and temp val at top is less than curr temp
            while stack and stack[-1][0] < currTemp:
                #pop temp and index vals
                popTemp, popIndex = stack.pop()
                #at that index, store index difference
                res[popIndex] = currIndex - popIndex
            stack.append((currTemp, currIndex))
        return res