import time
import os
from colorama import Fore, Back, Style


def splash():

    SECONDS = 10

    print(Fore.CYAN+ '')

    for progress in range(SECONDS+1):
        percent = (progress*100)//SECONDS
        print(("=======" * progress).center(80), str(percent).center(80))        
        print("\n")
        time.sleep(0.5)
        os.system('clear')

    #print("WELCOME".center(80))
    print(Style.RESET_ALL)
    