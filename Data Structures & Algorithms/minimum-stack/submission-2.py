class MinStack:

    def __init__(self):
        self.currMin = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        #if stack empty
        if not self.stack:
            self.stack.append(0) #append 0 as difference between val and min (same number)
            self.currMin = val #set min to val
        else:
            #append val - current min
            self.stack.append(val-self.currMin)
            #update current min if val smaller
            if val <= self.currMin:
                self.currMin = val
    def pop(self) -> None:
        #check empty
        if not self.stack:
            return
        #get popped value
        popped = self.stack.pop()
        #need to update min 
        if popped < 0:
            self.currMin -= popped

    def top(self) -> int:
        #get the top elem
        topElem = self.stack[-1]
        if topElem > 0:
            #input to stack was val - currMin so we need input + currMin
            return topElem + self.currMin
        #if top elem is 0 then no diff between elem and min
        #if top elem is negative then its the min so return min
        else:
            return int(self.currMin)


    def getMin(self) -> int:
        #return the min element
        return int(self.currMin)
