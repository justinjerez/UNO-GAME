from classes.player import *

from functions.abstracts import *


# Welcome presentation
clear_console()
welcome()

# Create players
players = []

# Players entry validation
while(True):
    try:
        num_of_players = int(input('\nWrite the num of players(2-4):'))
        
        if num_of_players > 4 or num_of_players < 2:
            raise TypeError

        clear_console()
        break

    except ValueError:
        print('You must insert an integer.')

    except TypeError:
        print('Entry out of range. Min 2 player - Max 4 players')

# Assign players names
count = 0
while count < num_of_players:
    name = input('Player {}: '.format(count + 1))

    if name == '':
        name = 'Player {}'.format(count + 1)

    # Create player
    Player(name)
    count += 1