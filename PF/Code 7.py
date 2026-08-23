# Task 1

i =0
found = False
word = "learning"
with open("Practise.txt","r")as f:
    for line in f:
        i += 1
        if word in line:
            print(f"Found word on line {i}")
            found = True
    if(not found):
        print("-1")


# Task 2

count = 0
with open("Practise_1.txt","r") as f:
    f.seek(0)
    for line in f:
        data = line
        data = data.split(",")
        for numbers in data:
           numbers = int(numbers)
           if(numbers % 2==0):
              count+=1

print("Total Even Numbers are ",count)


# Task 3

word = "Java"
replace_with = "Python"
with open("Practise.txt","r")as f:
    data = f.read()

data = data.replace(word,replace_with)

with open("Practise.txt","w") as f:
    f.write(data)

