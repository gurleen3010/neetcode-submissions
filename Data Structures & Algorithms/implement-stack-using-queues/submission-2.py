class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        if len(self.q1) == 0:
            return -1

        while len(self.q1) > 1:
            val = self.q1.popleft()
            self.q2.append(val)

        poppedValue = self.q1.pop()

        while len(self.q2) > 0:
            self.q1.append(self.q2.popleft())

        return poppedValue

    def top(self) -> int:
        if len(self.q1) == 0:
            return -1
            
        return self.q1[-1]

    def empty(self) -> bool:
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()