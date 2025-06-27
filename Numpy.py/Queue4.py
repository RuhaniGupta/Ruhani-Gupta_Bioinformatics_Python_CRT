'''Write a python program to create a customer services by adding the customer into the queue once the
 customer is served he has to be removed from the queue'''
class CustomerServiceQueue:
    def __init__(self):
        self.queue = []
    def add_customer(self, customer_name):
        self.queue.append(customer_name)
        print(f"{customer_name} added to the queue.")
    def serve_customer(self):
        if self.queue:
            served = self.queue.pop(0)
            print(f"{served} has been served and removed from the queue.")
        else:
            print("No customers to serve")
    def display_queue(self):
        if self.queue:
            print("Current queue:", " -> ".join(self.queue))
        else:
            print("The queue is empty")
service = CustomerServiceQueue()
service.add_customer("Ruhi")
service.add_customer("Sona")
service.add_customer("laduu")
service.display_queue()
service.serve_customer()
service.display_queue()
service.serve_customer()
service.serve_customer()
service.serve_customer()  