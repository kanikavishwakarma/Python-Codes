#  ************************ CUBE *********************************

print("Finding volume , surface area , lateral surface area of a cube")

class Cube:

    def __init__(self,side):
        self.side = side

    def Volume(self):
        return self.side* self.side* self.side

    def Surface_Area(self):
        return 6 * self.side * self.side

    def Lateral_Surface_Area(self):
        return 4 * self.side * self.side    

side = int(input("Enter side of cube : "))

c1 = Cube(side)
print("Volume of cube : ",c1.Volume())
print("Surface area of cube : ",c1.Surface_Area())
print("Lateral surface area of cube : ",c1.Lateral_Surface_Area())