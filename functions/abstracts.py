""" IMPORTS """
import time
from os import name, system

# Clean Consonsole
def clear_console():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

# Welcome presentation
def welcome():
    print('UNO GAME')
    time.sleep(1)
    print('By Justin Jerez')
    time.sleep(1)
    print('A Cincinnatus project')
    time.sleep(1)
    input('\n Press any key to start the game...')
    clear_console()