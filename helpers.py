#Auxiliar functions
#Funciones validadoras y eso

import re
import os, signal
import platform
from data import database_handler


#Function that detects the operating system and clean the terminal:
def clear():
    if platform.system() == 'Windows':
       os.system('cls')    
    else:
       #UNIX LIKE SYSTEM
       os.system('clear') 


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
    get_conn().commit()
    get_conn().close()


def get_all(table):
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
    conn = database_handler.Connection().connect()
    cursor = conn.cursor()

    if table == 'clients':
       cedula = rowid 
       cursor.execute('DELETE FROM {} WHERE cedula=?'.format(table), (cedula,))
       return True

    else:
       cursor.execute('DELETE FROM {} WHERE cedula=?'.format(table), (rowid,))    
       return True

    return False

        


if __name__=="__main__":   
   is_user('erick', 'EMem23')

#Documentation:
"""
>>> is_valid('22900274733')   #No valido, en uso 
False

>>> is_valid('A002229757833') #No valido, empieza con un caracter 
False

>>> is_valid('00178472411')   #Valido
True
"""