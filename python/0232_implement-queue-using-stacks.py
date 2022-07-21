class MyQueue:

    def __init__(self):
        self.qin = []
        self.qout = []

    def push(self, x: int) -> None:
        self.qin.append(x)

    def pop(self) -> int:
        if not self.qout:
            while self.qin:
                self.qout.append(self.qin.pop())
        if self.qout:
            return self.qout.pop()
        return None

    def peek(self) -> int:
        if self.qout:
            return self.qout[-1]
        if self.qin:
            return self.qin[0]
        return None

    def empty(self) -> bool:
        return not self.qin and not self.qout


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()