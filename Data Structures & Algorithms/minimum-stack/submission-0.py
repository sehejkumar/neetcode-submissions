class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minStack.append(val)
        else:
            self.stack.append(val)
            if self.minStack[-1] < val:
                self.minStack.append(self.minStack[-1])
            else:
                self.minStack.append(val)

    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()
            

    def top(self) -> int:
        top = self.stack[-1]
        return top
        

    def getMin(self) -> int:
        #simply return the minimum value
        return self.minStack[-1]
