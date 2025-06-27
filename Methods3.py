'''Write a python program to create a product class declare the class as product name,
 product id, price, gst, manufacture date and exprire date'''
class Product:
    def __init__(self, name, product_id, price, gst, manufacture_date, expire_date):
        self.name = name
        self.product_id = product_id
        self.price = price
        self.gst = gst
        self.manufacture_date = manufacture_date
        self.expire_date = expire_date
    def Get_details(self): 
        print(f"Product Name: {self.name}")
        print(f"Product ID: {self.product_id}")
        print(f"Price: {self.price}")
        print(f"GST: {self.gst}")
        print(f"Manufacture Date: {self.manufacture_date}")
        print(f"Expire Date: {self.expire_date}")
product1 = Product("Laptop", 101, 50000, 18, "2025-01-02", "2030-01-01")
product1.Get_details()


