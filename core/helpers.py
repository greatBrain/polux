#Auxiliar functions, database functions
#Funciones validadoras

import re
import os, signal
import platform
from database import database_handler
from colorama import Fore, Back, Style

#Function that detects the operating system and clean the terminal:
def get_conn(conn, cursor):
    conn = conn
    cursor = cursor


def clear():
    if platform.system() == 'Windows':
       os.system('cls')    
    else:
       #UNIX LIKE SYSTEM
       os.system('clear') 

def format_screen_confirmation():
    clear()
    
    while True: 
       print(Fore.RED + "")
       print("=======*=======*========".center(80))
       print("===========*============".center(80))
       print("=          *           =".center(80))
       print("=    SURE TO DELETE?   =".center(80))
       print("=          *           =".center(80))
       print("===========*============".center(80))
       print("=======*========*=======".center(80))
       print(Style.RESET_ALL)

       confirm = input("y/n:")

       if confirm=='y':
          return True
          break
       elif confirm=='n':
          return False
          break
       else:
          print("Incorrect option..")


def stop_program():
    if platform.system() == 'Windows':
       os.system("TASKKILL /F /IM cmd.exe")

    else:
       #UNIX LIKE SYSTEMS
       termina_pid = os.getpid()
       os.kill(termina_pid, signal.SIGSTOP)
       clear()

def valid_input(min_length, max_length):
    while True:
          text = input("> ")
          if len(text) >= min_length and len(text) <= max_length:
             return text
          else:
             print("No valido. Intente otra vez!")


def is_valid(cedula):
    if not re.match('[0-9]{11}', cedula):       
       return False
    return True


def is_user(name, password):
    conn = database_handler.Connection().connect()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM users WHERE user_name=? AND user_password=?''', (name,password,))
    data = cursor.fetchall()

    if data:
       return True
    else:
       return False  

             
def add_client(data=[]):
    conn = database_handler.Connection().connect()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO clients(client_name, client_last_name, cedula, email, phone) VALUES(?,?,?,?,?)', (data[0],data[1],data[2], data[3], data[4]))
    conn.commit()
    conn.close()


def add_product(data=[]):
    conn = database_handler.Connection().connect()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO products(product_name, product_price) VALUES(?,?)', (data[0],data[1]))
    conn.commit()
    conn.close()

def get_all(table, rowid=None):
    conn = database_handler.Connection().connect()
    cursor = conn.cursor()
    data=cursor.execute('''SELECT * FROM {}'''.format(table))
    return data


def get_client(cedula):
    int(cedula)
    conn = database_handler.Connection().connect()
    cursor = conn.cursor()
    data=cursor.execute('''SELECT * FROM clients WHERE cedula=?''', (cedula,))
    return data


def delete(table, rowid):
   
    int(rowid)    
    str(table)

    try:
       conn = database_handler.Connection().connect()
       cursor = conn.cursor()

       if table == 'clients':
          cedula = rowid 
          cursor.execute('''DELETE FROM clients WHERE cedula=?''', (cedula,))
          conn.commit()
          return True
       
       else:
          cursor.execute('DELETE FROM'+table+'WHERE rowid=?',(rowid,))   
          return True
    
    except Exception as e:
          print("Error.. ", e)
   
    finally:
          conn.close() 