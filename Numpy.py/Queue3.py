from collections import deque
queue = deque()
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue after enquering", queue)
first = queue.popleft()
print("Dequeued element:", queue)
print("Queue after denquering", queue)
if not queue:
    print("Queue is empty")
else:
        print("Queue is not empty")
print("Front element:", queue[0])

#For stacks
from collections import deque
stack = deque()
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack after pushing", stack)
top=stack.pop()
print("Popped element:", top)
print("Stack after popping", stack)
if not queue:
    print("Stack is empty")
else:
        print("Stack is not empty")
print("Top element:", stack[-1])