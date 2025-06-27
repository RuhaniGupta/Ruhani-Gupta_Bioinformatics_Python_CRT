#Write a python program to create a mobile class and declare a status of mobile as colour,price,branch,series,processor,Ram Create 10 objects and initialize using constructor print the details of the individual objects.
class Mobile():
    def __init__(self,colour,price,brand,series,version,ram,storage,processor,features,battery):
        print("Object is created")
        self.Colour=colour
        self.Price=price
        self.Brand=brand
        self.Series=series
        self.Version=version
        self.Ram=ram
        self.Storage=storage
        self.Processor=processor
        self.Features=features
        self.Battery=battery
def Display_Details(self):
    print(f"The colour of mobile is --->{self.Colour}")
    print(f"The colour of mobile is --->{self.Price}")
    print(f"The colour of mobile is --->{self.Brand}")
    print(f"The colour of mobile is --->{self.Series}")
    print(f"The colour of mobile is --->{self.Version}")
    print(f"The colour of mobile is --->{self.Ram}")
    print(f"The colour of mobile is --->{self.Storage}")
    print(f"The colour of mobile is --->{self.Processor}")
    print(f"The colour of mobile is --->{self.Features}")
    print(f"The colour of mobile is --->{self.Battery}")
M1=Mobile("Green",'5000','Samsung','S23','Android 15','8gb','128','13A','Ai','4500mah')
Display_Details(M1)