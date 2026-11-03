class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n

        step1 = 1
        step2 = 2
        for i in range(3, n+1):
            newSteps = step1+step2
            step1=step2
            step2 = newSteps

        return newSteps