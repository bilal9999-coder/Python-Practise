# Task 1
a,b,c = input("Enter your 3 favourite movies: "). split(",")
lis = [a,b,c]
print(lis)

# Task 2
list = [1,"abc","abc",1]
l1= list.copy() # As lis.copy return none so it was super necessory to copy the list and then reverse it
l1.reverse
if(list == l1):
    print("True, It is palindrome")
else:
    print("false")