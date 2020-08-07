from classes.card import Card
from classes.deck import Deck
from classes.player import Player

from functions.abstracts import *
from functions.functionality import *

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
        clear_console()
        print('You must insert an integer.')

    except TypeError:
        clear_console()
        print('Entry out of range. Min 2 player - Max 4 players')

# Assign players names
print('Insert players names\n')

count = 0
while count < num_of_players:
    player_name = input('Player {}: '.format(count + 1))

    if player_name == '':
        player_name = 'Player {}'.format(count + 1)

    # Create player
    players.append(Player(player_name))
    count += 1

clear_console()
""" CREATE PLAYERS - END """

# Creating decks
main_deck = Deck()
stock_deck = Deck()

# Cleaning stock
stock_deck.clear()

# Hand out / distribute cards
hand_out_cards(players, main_deck)

""" START THE GAME"""

GAME_OVER = False # Game state
current_turn = 0  # Current Turn
clockwise = True  # Defines the game flow

# Showing table card to start the game
move_card(main_deck, stock_deck, -1)
table = stock_deck.cards[-1]

# Validating first card on table
if table.suit == 'Wilds':
    # If first card on table is from wildcards suit, return it and shuffle again
    refill_deck(main_deck, stock_deck)
    move_card(main_deck, stock_deck, -1)
    table = stock_deck.cards[-1]

else:
    if table.value == '+2':
        print('First card on table is +2, first player takes them')
        input('\n Press any key to continue...')
        clear_console()

    elif table.value == 'reverse':
        print('First card on table is reverse, the game flow has changed')
        input('\n Press any key to continue...')
        clear_console()

    elif table.value == 'pass':
        print('First card on table is pass, first player turn has been skipped')
        input('\n Press any key to continue...')
        clear_console()

# START PLAYING
while not GAME_OVER:

    """  Some validation between turns """
    # If player has only a card must say uno to win
    if len(players[current_turn].cards) < 1:
        say_uno(players[current_turn].get_name())

    # If main deck ran out of cards, refill. If both deck ran out cards end the game
    if len(main_deck.cards) <= 4:
        if len(stock_deck.cards) >= 4:
            refill_deck(main_deck, stock_deck)
        else:
            print('\nRan out of cards')
            print('......GAME OVER......')
            break
    
    # Turn actions
    while True:
        try:
            # Showing player name
            print("\n{}'s turn".format(players[current_turn].get_name()))
            
            # Showing table
            print('\nTable:', table.show())

            #  showing player hand
            print("\n0: Take a card")
            players[current_turn].show_hand()

            # Selecting an action / take or throw a cards
            option = int(input('\nChoose a card from above: '))

            if option == 0:
                print('You took:', main_deck.cards[-1].show());

                if is_playable(main_deck.cards[-1], table):
                    print('Card is playable')
            else:
               if is_playable(players[current_turn].cards[option - 1], table):
                   print('Card is playable')
        
        except ValueError:
            pass
""" END THE GAME """