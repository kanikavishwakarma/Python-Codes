#  ************************ TRIANGLE *********************************
  
print("Finding area of a triangle")

class Triangle:

    def __init__(self,base,height):
        self.base = base
        self.height = height

    def Area(self):
        return 0.5 * self.base * self.height

b = int(input("Enter base : "))
h = int(input("Enter height : "))
T1 = Triangle(b,h)
print("Area of first triangle : ",T1.Area())


b = int(input("Enter base : "))
h = int(input("Enter height : "))
T2 = Triangle(b,h)
print("Area of second triangle : ",T2.Area())


                              



