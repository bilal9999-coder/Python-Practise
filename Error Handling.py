try:
   a = int(input("Please Enter an Integer Value: "))
   print("You Entered",a)
except Exception as e:
   print(e)

print("okey bye")

try:
   a = int(input("Please Enter An Integer Again: "))
   print("You Entered",a)
except:
   print("Error: ENTER A VALID INTEGER")

try:
   a = int(input("Please Enter An Integer from (1-10): "))
   if a not in range(1,11):
      raise ValueError("Invalid Number")
   print("You Entered",a)
except Exception as e:
    print(e)