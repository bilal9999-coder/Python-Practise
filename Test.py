def return_debt(line):
         data = line
         data = data.split()
         debt = int(data[1])
         return debt

with open("money.txt","r") as f:
    f.seek(0)
    for line in f:
        if "Abdullah" in line:
            print(return_debt(line) )               
        elif "Bilal" in line:
            print(return_debt(line) )