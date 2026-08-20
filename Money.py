a = int(input("Enter the Money Abdullah Paid Today: "))
b = int(input("Enter the Money Bilal Paid Today: "))

bmoney = 0
amoney=0
moneyb=0
money = 0

with open("money.txt","r") as f:
    f.seek(0)
    for line in f:
        if "Abdullah" in line:
            data = line
            data = data.split()
            money = int(data[2]) 
            if(money - a < 0):
                bmoney = a - money
                money = 0
            else:
                money = money - a


with open("money.txt","r") as f:
    f.seek(0)
    for line in f:
        if "Bilal" in line:
            data = line
            data = data.split()
            moneyb = int(data[2]) 
            moneyb += bmoney
            if(moneyb - b < 0):
                amoney = b - money
                moneyb = 0
            else:
                moneyb = money - b


with open("money.txt","w") as f:
    f.seek(0)
    f.write(f"\nBilal debt: {moneyb} Rs")
    f.write(f"\nAbdullah debt: {money} Rs")



if(amoney > 0):
           with open("money.txt","r") as f:
              f.seek(0)
              for line in f:
                if "Abdullah" in line:
                      data = line
                      data = data.split()
                      money = int(data[2]) 
                      money += amoney
                      if(money - a < 0):
                         bmoney = a - money
                         money = 0
                      else:
                         money = money - a

           with open("money.txt","w") as f:
                f.write(f"\nAbdullah debt: {money} Rs")
                f.write(f"\nBilal debt: {moneyb} Rs")

print("--------------- DEBTS DETAIL ---------------")
with open("money.txt","r") as f:
    for line in f:
        if "Bilal" in line:
             data = line
             data = data.split()
             name = data[0]
             cost = data[2]
             print(f"{name} needs to pay {cost} Rs")
        elif "Abdullah" in line:
            data = line
            data = data.split()
            name = data[0]
            cost = data[2]
            print(f"{name} needs to pay {cost} Rs")