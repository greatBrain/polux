#Source code, core of the app. Main module of the program.

from menu import Menu
from helpers import clear, close_program, is_user
from colorama import Fore, Back, Style

clear()

def login():
    count = 0

    while True:
        print(Fore.GREEN + "Login to Polux".center(80))
        print("\n")
        
        user = input("Username:")
        password = input("Password:")
        print(Style.RESET_ALL)    

        if is_user(user, password):
           Menu().loop()
           break

        else:
           if count >=3:
              print("Too much trying...") 
              stop_program()
           else:
              clear() 
              print(Fore.RED + "User invalid, try again...".center(80))
              count += 1
              print(Style.RESET_ALL)  
                

if __name__=="__main__":
   login() 