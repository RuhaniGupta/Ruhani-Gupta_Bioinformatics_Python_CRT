class Graduation:
    def __init__(self):
        pass
    @staticmethod
    def Graduate():
        print("Congratualtions you are a Computer science graduate")
class CSE(Graduation):
    def __init__(self):
        pass
    @staticmethod
    def Graduate():
        print("Congratualtions you are a Computer science graduate")
class Bioinformatics():
    def __init__(self):
        pass
    @staticmethod
    def Graduate():
        print("Congratualtions you are a Bioinformatics graduate")
class ECE():
    def __init__(self):
        super().__init__()
    @staticmethod
    def Graduate():
        print("Congratualtions you are a ECE graduate")
Graduation.Graduate()
CSE.Graduate()
Bioinformatics.Graduate()
ECE.Graduate()


