class Stack:
    def __init__(self):
        self.values = []

    def push(self, val: int):
        self.values.append(val)

    def pop(self):
        if len(self.values):
            return self.values.pop()
        
    def peek(self):
        if self.values:
            return self.values[-1]



