from colorama import Fore,Back,Style,init
import os
import sys

# Some GPT Shit For Fixing a Thing -------------------------------------

# This automatically finds the correct folder whether running as a .py script or a compiled .exe
if getattr(sys, "frozen", False):
  # If running as an .exe, get the folder where the .exe is located
  base_path = os.path.dirname(sys.executable)
else:
  # If running normally as a python script
  base_path = os.path.dirname(os.path.abspath(__file__))

# Build the absolute path to money.txt
money_file_path = os.path.join(base_path, "money.txt")

# -----------------------------------------------------------------------


init(autoreset=True)

# Variables
b_future_debt = 0
debt_a = 0
debt_b = 0
a_future_debt = 0


# Functions
def return_debt(str):
         data = str
         data = data.split()
         debt = int(data[1])
         return debt

def display ():
         with open(money_file_path,"r") as f:
              f.seek(0)
              for line in f:
                     data = line
                     data = data.split()
                     if "Abdullah" in line:
                          print(Back.RED + f"{data[0]} needs to pay {data[1]} to Bilal")
                     elif "Bilal" in line:
                          print(Back.RED + f"{data[0]} needs to pay {data[1]} to Abdullah")


# main ()
print(Fore.GREEN + "--------------- Current Situation --------------")
display()
try:
    a = int(input("\n\nEnter the Money Abdullah Paid Today: ")) 
    b = int(input("Enter the Money Bilal Paid Today: ")) 
except:
    print(Fore.RED + Style.BRIGHT + "ValueError: Please Enter a Valid Integer")

# Debt Calculation
with open(money_file_path,"r") as f:
    f.seek(0)
    for line in f:
        if "Abdullah" in line:
            if(return_debt(line) - a < 0):       # -- (0 - 1000)
                b_future_debt = a - return_debt(line)    # b_future = 1000 - 0 = 1000
                debt_a = 0                               # debt_a = 0
            else: 
                debt_a = return_debt(line) - a                  
        elif "Bilal" in line:
            debt_b = return_debt(line) + b_future_debt          # debt_b = 30 + 1000
            if(debt_b - b < 0):                                  
                a_future_debt = b - debt_b                   
                debt_b = 0       
                debt_a = a_future_debt                           
            else:                                               
                debt_b = debt_b - b                             # debt_b = 1030 - 0 = 1030

# Adding New Data
with open(money_file_path,"w") as f:                    
    f.seek(0)
    f.write(f"Bilal {debt_b}")                  
    f.write(f"\nAbdullah {debt_a}")

print(Fore.GREEN +"\n\n--------------- DEBTS DETAIL ----------------")
display()
print("\n\n")

a = input(Back.GREEN +"\nPress Enter to exit...")
