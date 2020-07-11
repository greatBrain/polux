#Source code, core of the app. Main module of the program.

from menu import Menu
#from data.database_handler import Connection


def main():
    Menu().loop()

if __name__=="__main__":
   main() 