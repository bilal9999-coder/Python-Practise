B = "Bilal"
Z= "Zain"
B_Score = 0
Z_Score = 0
Updated = []

def changeScoreSingle (name:str, new_score:int) -> None:
    with open("Score.txt", "r") as f:
         for line in f:
             if name in line:
                 Updated.append(f"{name} {new_score}")
             else:
                 Updated.append(line)

def changeScoreBoth (name_b:str, name_z:str, new_score_B:int, new_score_Z:int ) -> None:
    with open("Score.txt", "r") as f:
         for line in f:
             if name_b in line:
                 Updated.append(f"{name_b} {new_score_B}")
             elif name_z in line:
                 Updated.append(f"{name_z} {new_score_Z}")

def getScore ():
    with open("Score.txt", "r") as f:
      global B,Z,B_Score,Z_Score
      for line in f:
         data = line
         if B in line:
            data = data.split()
            B_Score = int(data[1])
         elif Z in line:
            data = data.split()
            Z_Score = int(data[1])


def addtoData ():
      global Updated
      with open("Score.txt", "w") as f:
            for words in Updated:
                 f.writelines(f"{words}\n")

getScore()

print(f"Current Score of Bilal is {B_Score}")
print(f"Current Score of Zain is {Z_Score}")
choice = int(input("Do you want to change the score: \nPress 1 for Yes\nPress 2 for No\nPress: "))
if(choice == 1):
    print("1) Change Bilal Score Only")
    print("2) Change Zain Score Only")
    print("3) Change Both Scores")
    choice_2 = int(input("Press: "))
    if(choice_2 == 1):
          score = int(input(f"Enter the new score for {B}: "))
          changeScoreSingle(B,score)
          addtoData()
          getScore()
          print(f"\n\nUpdated Score of Bilal is {B_Score}")
          print(f"Score of Zain is {Z_Score}\n\n")
    elif(choice_2 == 2):
          score = int(input(f"Enter the new score for {Z}: "))
          changeScoreSingle(Z,score)
          addtoData()
          getScore()
          print(f"\n\nScore of Bilal is {B_Score}")
          print(f"Updated Score of Zain is {Z_Score}\n\n")
    elif(choice_2 == 3):
          score_b = int(input(f"Enter the new score for {B}: "))
          score_z = int(input(f"Enter the new score for {Z}: "))
          changeScoreBoth(B,Z,score_b,score_z)
          addtoData()
          getScore()
          print(f"\n\nUpdated Score of Bilal is {B_Score}")
          print(f"Updated Score of Zain is {Z_Score}\n\n")         
    else:
         print("Wrong Input")
    

print("Thanks for running the code")
