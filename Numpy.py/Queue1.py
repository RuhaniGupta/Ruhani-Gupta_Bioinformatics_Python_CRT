class Queue:
    def __init__(self):
        self.items=[]
    #Add items to rear(end)
    def enqueue(self,item):
        self.items.append(item)
    #Check Queue is empty or not
    def is_empty(self):
        return len(self.items)==0
    #Remove and return front item
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)
    #Look at front item without removing
    def peek_front(self):
        if self.is_empty():
            return None
        return self.items[0]
    #Look at rear items without removing
    def peek_rear(self):
        if self.is_empty():
            return None
        return self.items[-1]
    def size(self):
        return len(self.items)
    def Display(self):
        print(self.items)
Queue=Queue()
print("initial stack contain elements of:")
Queue.enqueue(10)
Queue.enqueue(20)
Queue.enqueue(30)
Queue.Display()
Queue.dequeue()
Queue.peek_front()
Queue.size()
Queue.Display()   


        