#Define a class for a Circle with methods to calculate its  
#area and circumference.

class circle:

    def __init__(self,radius):
        self.radius=radius

    def Area(self):
        return 3.14*pow(self.radius,2)
    
    def circumference(self):
        return 2*3.14*self.radius
    

radius=int(input("Enter radius: "))

c1=circle(radius)
print(c1.Area())
print(c1.circumference())
        

