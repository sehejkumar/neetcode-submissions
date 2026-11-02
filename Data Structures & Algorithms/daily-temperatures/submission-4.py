class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, currTemp in enumerate(temperatures):
            while stack and currTemp > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            
            stack.append(i)

        return res
            


