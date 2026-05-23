class MinStack:

    def __init__(self):
        self.minStack=[]
        self.stack = []

    def push(self, val: int) -> None:
        #append to actual stack
        self.stack.append(val)
        #two arrays corresponding indicies are min up until that index
        minVal = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(minVal)
    def pop(self) -> None:
        #simply pop from both
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        #return the top element in the min stack
        #it will hold minimum element for whole stack]
        return self.minStack[-1]
