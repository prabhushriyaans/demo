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
class Queue:
    def __init__(self):
        self.q=[]
    def enqueue(self,x): 
        self.q.append(x)
    def dequeue(self): 
        if self.q is None:
            print("The Queue is Empty")
        else:
            return self.q.pop(0)
    def front(self):
        if self.q is None:
            print("The Queue is Empty")
        else:
            return self.q[0]
            
    def back(self):
        if self.q is None:
            print("The Queue is Empty")
        else:
            return self.q[-1]

# class Linked_list:
#     def __init__(self):
        