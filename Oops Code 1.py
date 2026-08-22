class Student:
     ...

class Person:
     def __init__ (self,name,age):
          self.n = name # here it will call the func 
          self.age = age
     def __str__ (self):
          return f"{self.n} is {self.age} years old"
     # As explained in (C2) so we do this
     @property
     def n(self):
          return self._n   # as the name of func and var is same (it is must as otherwise the stu.n will not call this func as it will have a different name)
     @n.setter                                        # so we use _ before the var name
     def n (self, name):
          if not name:
               raise ValueError("Missing Name")
          self._n = name
     
def main ():
     # First Class
     stu = Student()
     stu.name = "Bilal"
     stu.age = 19
     print(f"{stu.name} is {stu.age} years old")
     # Second Class
     stu = Person("Zain",16)
    #  stu.n = ""  # but i can accidently do that (C2) # it will ensure the right input
     print(stu)
     #b But i can still do that
     stu._n =''
     print (stu)

     

if __name__ == "__main__":
     main()

