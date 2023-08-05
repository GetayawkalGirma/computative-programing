class MinStack:
    def __init__(self):
        self.stack=list()
        self.minstack=[]
    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.minstack or value <= self.minstack[-1]:
            self.minstack.append(value)
    def pop(self)-> None:
        popped= self.stack.pop(-1)
        if popped == self.minstack[-1]:
            self.minstack.pop()
    def getMin(self)-> int:
        return self.minstack[-1]
    def top(self)-> int :
        return self.stack[-1]
