class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_len = 0

    def push(self, val: int) -> None:
        if self.stack_len == 0:
            self.stack.append((val, val))
        else:
            new_min = min(self.stack[-1][1], val)
            self.stack.append((val, new_min))
        self.stack_len += 1

    def pop(self) -> None:
        del self.stack[-1]
        self.stack_len -= 1

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
    

    


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()