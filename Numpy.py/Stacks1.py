class Stack:
    def __init__(self):
        self.Stack=[]
    def push(self,data):
        self.Stack.append(data)
        print(f"{data}Element is Appended")
    def isempty(self):
        if len(self.Stack)==0:
            return True
    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            self.Stack.pop()
            print("Element is Removed")
    def Display(self):
        for i in self.Stack:
            print(i)
stack=Stack()
stack.push(100)
stack.push(104)
stack.push(120)
stack.push(156)
stack.Display()