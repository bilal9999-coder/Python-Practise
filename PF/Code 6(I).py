# TASk 1

list = ["zain","bilal", "Aisha", "Hasfsa"]

def listlen (list):
       print(len(list))

listlen(list)


# TAsk 2

def printl(list):
    for el in list:
          print(el,end=" ")

printl(list)


# Task 3

def fac (n=5):
     fact = 1
     for num in range (1,n+1):
           fact = fact * num
     print("\nFactorial of 5 is: ", fact)

fac()

# Task 4

def convert(n):
      n = n  /300
      return n

print("600RS in usd is ",convert(600))