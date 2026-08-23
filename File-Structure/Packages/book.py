class Book:
    def __init__ (self,name,author):
        self.name = name
        self.author = author
    def __str__ (self):
        return f"{self.name} from {self.author}"

def hello (str):
       return f"Hello! {str}"

B1 = {'Name' : 'HOTD'}
