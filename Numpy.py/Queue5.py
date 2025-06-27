'''write a python program to take the length of queue as input from the user and add the elements by using 
enqueue method and print the elements present in the queue and remove the elements 1 by 1 from the queue 
and check whether the queue is empty or not and print front peek and rear peek'''
class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size
    def is_empty(self):
        return len(self.queue) == 0
    def is_full(self):
        return len(self.queue) == self.size
    def enqueue(self, item):
        if not self.is_full():
            self.queue.append(item)
            print(f"Enqueued: {item}")
        else:
            print("Queue is full. Cannot enqueue.")
    def dequeue(self):
        if not self.is_empty():
            removed = self.queue.pop(0)
            print(f"Dequeued: {removed}")
            return removed
        else:
            print("Queue is empty. Cannot dequeue.")
            return None
    def front_peek(self):
        if not self.is_empty():
            return self.queue[0]
        return None
    def rear_peek(self):
        if not self.is_empty():
            return self.queue[-1]
        return None
    def display(self):
        print("Queue contents:", self.queue)
# Main program
length = int(input("Enter the length of the queue: "))
q = Queue(length)
for i in range(length):
    element = input("Enter an element to enqueue: ")
    q.enqueue(element)
q.display()
print(f"Front Peek: {q.front_peek()}")
print(f"Rear Peek: {q.rear_peek()}")
while not q.is_empty():
    q.dequeue()
print("Is the queue empty", q.is_empty())