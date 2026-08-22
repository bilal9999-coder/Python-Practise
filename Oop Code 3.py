# Ok Now Operator Overloading
class Vector:
    def __init__ (self,real,img):
        self.real = real
        self.img = img

    def __add__(self,other):
        real = self.real + other.real
        img = self.img + other.img
        return Vector(real,img)
         
    def __str__(self):
        return f"{self.real} + {self.img}i"
    
v1 = Vector(10,20)
v2 = Vector(-2,0)
v3 = v1 + v2
print(v3)