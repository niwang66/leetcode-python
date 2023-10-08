import math

#https://leetcode.cn/problems/min-stack/submissions/
class MinStack:
    def __init__(self):
        self.stack = []
        self.min = math.inf
    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min:
            self.min = val
    def pop(self) -> None:
        if len(self.stack) > 0:
            val = self.stack.pop()
        min = math.inf
        for i in self.stack:
            if i < min:
                min = i
        self.min = min
    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
    def getMin(self) -> int:
        return self.min

if __name__ == '__main__':
    obj = MinStack()
    obj.push(1)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()