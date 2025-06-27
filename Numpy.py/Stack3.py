class Stack():
    def __init__(self): # Corrected the constructor name
        self.Stack=[]
    def push(self,data):
        self.Stack.append(data)
        print(f"{data} is added to stack")
    def isempty(self):
        if len(self.Stack)==0:
            return True
    def pop(self):
        if self.isempty():
            print("stack is empty")
        else:
            self.Stack.pop()
            print("element is removed")
    def peek(self):
        Len=len(self.Stack)
        print(f"peek element is{self.Stack[Len-1]}")
    def size(self):
        l= len(self.Stack) #For Size
        print(f"size of stack is {l}")
    def Display(self):
        self.Stack.reverse()
        Str=[]
        for i in self.Stack:
            Str.append(i)
        Rev_Str="".join(Str)
        print(Rev_Str)
stack=Stack()
stack.push("M")
stack.push("A")
stack.push("D")
stack.push("H")
stack.push("U")
print("initial stack contain elements of:")
stack.Display()
stack.pop()
stack.peek()
stack.size()
stack.Display()