'''Option menu'''

import os
import helpers
from data.database_handler import Connection
from manager import Manager
from colorama import Fore, Back, Style


class Menu:

     def loop(self):    
         
         while True:
             helpers.clear()                     

             print(Back.YELLOW + Fore.BLACK + "================================".center(80))
             print(Style.RESET_ALL)
             print("Clients & Products CLI Manager".center(80))
             print("\n")
             print("[1] Show all clients          ".center(80), "\n")
             print("[2] Search for client         ".center(80), "\n")
             print("[3] Add client                ".center(80), "\n")
             print("[4] Edit client               ".center(80), "\n")
             print("[5] Delete cliente            ".center(80), "\n")
             print("[6] Add product               ".center(80), "\n")
             print("[7] Exit                      ".center(80), "\n")
             print(Back.YELLOW + Fore.BLACK  + "================================".center(80))    
             print(Style.RESET_ALL)

             option = input(">")
             helpers.clear()                

             if option == '1':
                #TODO
                Manager().show_data('clients')

             elif option == '2':
                cedula = input("Write the client cedula:\n")
                
                if helpers.is_valid(cedula):
                   Manager().find_client(cedula) 
                else:
                   print(Fore.RED + "Cedula is not valid...".upper())  

             elif option == '3':
                Manager().add_client()
                print("Added sucessfully..".upper())

             elif option == '4':
                 if Manager().edit():
                    print("Done sucessfully...".upper())
                 else:
                    print("Something is worong, try again...".upper())    

             elif option == '5':
                  cedula = int(input("Cedula:"))

                  if Manager().delete_client(cedula)==True:
                     print("Deleted Sucessfully".upper())
                  else:
                     print("Something is worong, try again...".upper())

             elif option == '6':
                  if Manager().add_product()==True:  
                     print("Product created!".upper())
                     
             elif option == '7':
                  break
                  Connection().connect().close()

             input("\nPress ENTER to continue...") 
