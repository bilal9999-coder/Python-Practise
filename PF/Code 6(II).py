# Task 1

def sum (n): 
    if (n == 0):
        return 0
    s = n + sum(n-1)
    return s

print("Sum of first 3 natural no is ",sum(5))

# Task 2

list = [1,2,3,4,5]

def printlist(list,index):
    if(index > 0):
        printlist(list,index-1)
    print(list[index])

printlist(list,4)