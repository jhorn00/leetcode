#!/usr/bin/python3

# Time: O(1), each operation is constant time
# Space: O(n), stores a separate stack of mins, which could be up to n in size, as well as storing the stack of n size

class MinStack:

    def __init__(self):
        self.stack = []
        self.minVals = []

    def push(self, val: int) -> None:
        # if there is no min or it is the new min, add to minVals
        if not self.minVals or val <= self.minVals[-1]:
            self.minVals.append(val)
        # add to actual stack
        self.stack.append(val)
        

    def pop(self) -> None:
        if self.stack.pop() == self.minVals[-1]:
            self.minVals.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVals[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
