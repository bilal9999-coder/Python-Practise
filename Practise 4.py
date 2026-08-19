import os

with open("file.txt","w+") as f:
    f.write("Hello! How are you")


with open("file.txt","r") as f:
    print(f.read())

    
data = "Zain Score: 150\nBilal Score: 100\nAisha Score: 90"

with open("file.txt","w") as f:
    f.write(data)


def findRecord(file,st):
     file.seek(0)  # Reset file cursor to the beginning before searchin
     for line in file:
        if st in line:
            print(line)


with open("file.txt", "r") as f:
    choice = int(input("Hows data you want to read:\n1) Bilal\n2) Zain\n3) Aisha\n Enter: "))
    if(choice == 1):
        findRecord(f,"Bilal")
    elif(choice == 2):
        findRecord(f,"Zain")
    else:
        findRecord(f,"Aisha")

name_to_update = "Bilal"
new_score = 200


# 1. Read all lines and modify the matching line
lines = []
with open("file.txt", "r") as f:
    for line in f:
        if name_to_update in line:
            lines.append(f"{name_to_update} Score: {new_score}\n")
        else:
            lines.append(line)

# 2. Overwrite the file with updated data
with open("file.txt", "w") as f:
    f.writelines(lines)

print(f"Updated {name_to_update}'s score to {new_score}!")


txt = input("ENter the name you want to add more: ")
sc = int (input("ENter its Score: "))

with open("file.txt", "a+") as f:
    f.write(f"\n{txt} Score: {sc}")
