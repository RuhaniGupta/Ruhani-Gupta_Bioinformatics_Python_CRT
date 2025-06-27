#Delete the first node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def delete_front(self):
        if self.head:
            print(f"Deleting node with value: {self.head.data}")
            self.head = self.head.next
        else:
            print("List is empty. Nothing to delete.")
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
# Example usage:
ll = LinkedList()
ll.insert_front(30)
ll.insert_front(20)
ll.insert_front(10)
print("Initial list:")
ll.display()
ll.delete_front()
print("After deleting front node:")
ll.display()
   
