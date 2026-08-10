# Task 3

eng = int(input("Enter your marks in english: "))
urdu = int(input("Enter your marks in urdu: "))
maths = int(input("Enter your marks in maths: "))

dic= {}
dic["English"] = eng
dic["Urdu"] = urdu
dic.update({"Maths": maths})

print(dic)

# Task 4

set = set()
set.add(9)
set.add('9.0')

print(set)