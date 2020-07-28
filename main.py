from classes.card import Card
from classes.deck import Deck
from classes.player import Player

from functions.abstracts import *

# Welcome presentation
clear_console()
welcome()

""" CREATE PLAYERS - START """
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
print('Insert players names\n')

count = 0
while count < num_of_players:
    player_name = input('Player {}: '.format(count + 1))

    if player_name == '':
        player_name = 'Player {}'.format(count + 1)

    # Create player
    Player(player_name)
    count += 1

    clear_console()
""" CREATE PLAYERS - END """

# Creating decks
main_deck = Deck()
stock_deck = Deck() 

# Cleaning stock
stock_deck.clear()

