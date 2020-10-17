class carInfo:
    # Class variable
    wheels = 4

    def test(self):
        print("Hello Test")

    # price is a instance variable [variable inside method or inside constructor]
    def setPrice(self, price):
        self.price = price
        print(price)

    def getPrice(self):
        return self.price


obj1 = carInfo()
obj1.setPrice(100)
print(obj1.getPrice())


# Constructor in Python
class student:
    number_of_Students = 10;

    def __init__(self):
        print("constructor called")
    def __init__(self, girlCount):
        print("Second Constructor Called")
        self.girlCount = girlCount

    def setCount(self, active):
        self.active = active
    def getCount(self):
        return self.active

obj2 = student(10)

#   blank class
class blankclassdemo:
    def test23(self):
        print("Hello Blank Demo")
    pass
obj3 = blankclassdemo()
obj3.test23()


