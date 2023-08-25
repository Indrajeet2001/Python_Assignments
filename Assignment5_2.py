
class Circle:
    PI = 3.14
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0
    
    def Accept(self,value):
        self.Radius = value

    def CalculateArea(self):
        self.Area = self.PI * self.Radius * self.Radius
    
    def CalculateCircumference(self):
        self.Circumference = 2 * self.PI * self.Radius

    def Display(self):
        print("Value of radius is : ",self.Radius)
        print("Value of Area is : ",self.Area)
        print("Value of Circumference is : ",self.Circumference)

def main():

    rad = int(input("Enter the value of radius : "))

    obj1 = Circle()

    obj1.Accept(rad)
    obj1.CalculateArea()
    obj1.CalculateCircumference()

    obj1.Display()

if __name__ == "__main__":
    main()