# Task 1

Name = input("Enter your name: ")
print(len(Name))

# Task 2

str = "Hello, I had $400 dollars and i spent $100 from it the remaining is "
print(str+ "\b",400-300,"$")
print("Total $ in string is", str.count("$")+1)

#Task 3
no = int(input("Enter a number: "))
if(no % 2 == 0):
    print("Even")
else:
    print("odd")

#Task 4

n1 = int(input("Enter three numbers: "))
n2= int(input())
n3= int(input())

if(n1>=n2):
    if(n1>=n3):
       print(n1,"is the greatest number")
elif (n2>=n1 and n2>=n3):
       print(n2,"is the greatest number")
else:
       print(n3,"is the greatest number")

# Task 5

no = int(input("Enter a number: "))
if(no % 7 == 0):
     print("Number is multiple of 7")
else:
     print("Number is not multiple of 7")