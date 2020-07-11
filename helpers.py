#Auxiliar functions
#Funciones validadoras y eso

import re
import os
import platform
from data import database_handler
from tkinter import Tk


#Function that detects the operating system and clean the terminal:
def clear():
    if platform.system() == 'Windows':
       os.system('cls')    
    else:
       os.system('clear') #UNIX LIKE SYSTEM


def get_secreen_width():
    screen_width = Tk().winfo_screenmmwidth()
    middle_screen = screen_width/2
    return middle_screen

def valid_input(min_length, max_length):
    while True:
          text = input("> ")
          if len(text) >= min_length and len(text) <= max_length:
             return text
          else:
             print("No valido. Intente otra vez!")


def is_valid(cedula):
    #Comprueba que la cedula empieze con enteros del cero al nueve y que sean tres numeros:
    if not re.match('[0-9]{11}', cedula):       
       return False
    return True

def user_exist(name, password):
    conn = database_handler.Connection().connect()
    cursor = conn.cursor()
    data=cursor.execute('''SELECT * FROM user WHERE user_name=? AND password=?''', (name, password,))    

    if data:
       conn.close()
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
    #conn = database_handler.Connection().connect()
    #cursor = conn.cursor()
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
   pass

#Documentation:
"""
>>> is_valid('22900274733')   #No valido, en uso 
False

>>> is_valid('A002229757833') #No valido, empieza con un caracter 
False

>>> is_valid('00178472411')   #Valido
True
"""