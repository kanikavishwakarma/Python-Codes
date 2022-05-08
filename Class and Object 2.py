#  ************************ CIRCLE *********************************
         
print("Finding area and circumference of circle")

class Circle:

    def __init__(self,radius):
        self.radius = radius

    def Area(self):
          return 2* 3.14 * self.radius 

    def Circumference(self):
          return 3.14 * self.radius * self.radius

c1 = Circle(2)
print("Area of first circle : ",c1.Area())
print("Circumference of first circle : ",c1.Circumference())
c2 = Circle(4)
print("Area of second circle : ",c2.Area())
print("Circumference of second circle : ",c2.Circumference())