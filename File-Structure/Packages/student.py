class Student:
    def __init__ (self,name,course):
        self.name = name
        self.course = course
    def __str__ (self):
        return f"{self.name} doing {self.course}"
    def sort (self):
         return f"{self.name} is no 1"
        