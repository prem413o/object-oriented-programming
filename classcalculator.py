#Create a class to represent a basic calculator with add,  
#subtract, multiply, and divide methods.

class calculator:

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def Add(self):
        return self.a + self.b
    
    def  subtract(self):
        return self.a - self.b
    
    def multiply(self):
        return self.a * self.b
    

s1=calculator(45,5)
print(s1.Add())
        