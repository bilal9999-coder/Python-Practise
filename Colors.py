from colorama import Fore,Back,Style,init
init(autoreset=True)

print(Fore.GREEN + Back.BLACK+ "Working! ")
print(Fore.RED+ Style.BRIGHT + "Not Working! ")

m = "Hello Bilal"
print(Fore.WHITE + Style.DIM + f"{m}")