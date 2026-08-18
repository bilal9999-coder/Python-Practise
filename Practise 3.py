a = int(input("Enter the total students: "))
i =0
list = []

for i in range(0,a):
    name= input("Enter the name: ")
    age = input("Enter the age: ")
    dep = input ("Enter the department: ")
    record = {}
    record["Name"]= name
    record["Age"]= age
    record["Department"]= dep
    list.append(record)

for el in list:
     print(el)