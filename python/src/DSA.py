class Stack:
    def __init__(self):
        self.s=[]
    def push(self,x):
        self.s.append(x)
    def pop(self):
        if len(self.s)==0:
            return "Stack is empty"
        else:
            return self.s.pop()
    def top(self):
        if len(self.s)==0:
            return "Stack is empty"
        else:
            return self.s[-1]
