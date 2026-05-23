class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #return array of days until next is warmer
        res = [0] * len(temperatures)
        stack = [] #store index,temp
        for currIndex, currTemp in enumerate(temperatures):
            #while stack not empty and temp val at top is less than curr temp
            while stack and currTemp > temperatures[stack[-1]]:
                #pop temp and index vals
                popIndex = stack.pop()
                #at that index, store index difference
                res[popIndex] = currIndex - popIndex
            stack.append(currIndex)
        return res