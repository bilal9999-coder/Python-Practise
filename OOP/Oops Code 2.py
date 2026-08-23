# now i donot want to make multiple objects of my class i want only one so
import random

class Hat:
    School = ["Kips","PGC", "GCU", "Aspire", "Aps"]
    @classmethod
    def sort(cls,person):
        print(f"{person} is a good guy")
        print("He is going to", random.choice(cls.School))

class Grade:
    def __init__(self, grade):
        self.grade = grade

    @classmethod
    def get_input(cls):
       grade = input("Please enter your grade (A-F): ")
       return(cls(grade))

    def compliments (self):
        match self.grade:
            case 'A':
                print("Topper")
            case 'B':
                print("Good Work")
            case 'C':
                print("Only Satisfactory")
            case 'D':
                print("Work Hard")
            case 'E':
                print("How did you pass?")
            case 'F':
                print("Repeat Again ")
            case _:
                print("Enter Again!")


Hat.sort("Zain")
marks = Grade.get_input()
marks.compliments()
