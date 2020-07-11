'''Clients manager'''

import re
import helpers
from colorama import Fore, Back, Style

class Manager:
      def __init__(self):
          self.clients = []

      def add_client(self):
          #self.client = dict()

          print("Digite el nombre (de 2 a 20 caracteres)")
          self.name = helpers.valid_input(2, 20)
          
          print("Digite el apellido (de 2 a 20 caracteres)")
          self.last_name = helpers.valid_input(2, 20)
          

          while True:
               print("Digite el numero de cedula (11 numeros enteros)")
               cedula = helpers.valid_input(11, 11)

               if helpers.is_valid(cedula):
                  self.cedula = cedula
                  break

               print("Cedula incorrecta")

          self.email = input("e-mail address:")
          self.phone = input("phone number:")
          

          client_data = [self.name, self.last_name, self.cedula, self.email, self.phone]
          self.clients = client_data
          helpers.add_client(self.clients)


      def show_data(self, table):  
          client_data = helpers.get_all(table)

          #Show colored TITLES
          print(Fore.GREEN + "CLIENTS INFORMATION".center(80))
          print(Style.RESET_ALL)

          for client in client_data:
              print(*client, "\n", sep=', ')


      def find_client(self, cedula):
          helpers.get_client(cedula)
          client_data = helpers.get_client(cedula)

          #Show colored TITLES
          print(Fore.GREEN + "\n", "CLIENT INFORMATION".center(80))
          print(Style.RESET_ALL)

          for client in client_data:
              print(*client, "\n", sep=', ')



      

def edit():

    i, client= find()

    if client:
       print(f"Nuevo nombre de el cliente:({client['nombre']})")
       clients[i]['nombre'] = helpers.valid_input(2, 20)

       print(f"Nuevo apellido de el cliente:({client['apellido']})")
       clients[i]['apellido'] = helpers.valid_input(2, 20)

       return True

    return False    

def delete():

    i, client= find()

    if client:
       client = clients.pop(i)
       return True

    return False 

if __name__=="__main__":
   #import doctest
   #doctest.testmod() '''
   pass