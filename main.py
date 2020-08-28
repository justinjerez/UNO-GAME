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
        players_num = int(input('\nWrite the num of players(2-4):'))

        if players_num > 4 or players_num < 2:
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
while count < players_num:
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
ct_turn = 0  # Current Turn
clockwise = True  # Defines the game flow

# Moving a card to the table
move_card(main_deck, stock_deck, -1)
table = stock_deck.cards[-1]

# Validating first card on table
if table.suit == 'Wilds':
    # If first card on table is from wildcards suit, return it and shuffle again
    while table.suit == 'Wilds':
        refill_deck(main_deck, stock_deck, players)
        move_card(main_deck, stock_deck, -1)
        table = stock_deck.cards[-1]

else:
    # If first card on table is an action card carry out the action
    if table.value == '+2':
        print('First card on table is +2, first player takes them')
        for i in range(0, 2):
            move_card(main_deck, players[ct_turn], -1)
        input('\n Press any key to continue...')
        clear_console()

    elif table.value == 'reverse':
        print('First card on table is reverse, the game flow has changed')
        ct_turn = len(players) - 1
        clockwise = False
        input('\n Press any key to continue...')
        clear_console()

    elif table.value == 'pass':
        print('First card on table is pass, first player turn has been skipped')
        ct_turn += 1
        input('\n Press any key to continue...')
        clear_console() 

# START PLAYING
while not GAME_OVER:

    """  Some validation between turns """
    # If player has only a card must say uno to win
    if len(players[ct_turn].cards) < 1:
        say_uno(players[ct_turn].get_name())

    # If main deck ran out of cards, refill. If both deck ran out cards end the game
    refill_deck(main_deck, stock_deck, players)
    
    # Turn actions
    while True:
        try:
            # Showing player name
            print("\n{}'s turn".format(players[ct_turn].get_name()))
            
            # Showing table
            print('\nTable:', table.show())

            #  showing player hand
            print("\n0: Take a card")
            players[ct_turn].show_hand()

            # Selecting an action / take or throw a cards
            position = int(input('\nChoose a card from above: '))

            if position > len(players[ct_turn].cards) or position < 0:
                raise TypeError

            else:
                # Looking for the next player and the game direction in the next turn
                next_player, clockwise = next_turn(players, ct_turn, clockwise, stock_deck.cards[-1])

                if position == 0:
                    print('\nYou took:', main_deck.cards[-1].show());

                    if is_playable(main_deck.cards[-1], table):
                        print("The Card has been played")
                        # moving card from deck to stock
                        move_card(main_deck, stock_deck, -1)

                        # Doing the actions of the card action if the last card was a card action
                        table = carry_out_action(players[ct_turn], players[next_player], main_deck, stock_deck, table)

                    else:
                        print("The Card can't be played")
                        # moving card from deck to player's hand
                        move_card(main_deck, players[ct_turn], -1)

                else:
                    print('\nYou chose:', players[ct_turn].cards[position - 1].show());

                    if is_playable(players[ct_turn].cards[position - 1], table):
                        print("The Card has been played")
                        # moving card from player's hand to stock
                        move_card(players[ct_turn], stock_deck, position - 1)
                        
                        # Doing the actions of the card action if the last card was a card action
                        table = carry_out_action(players[ct_turn], players[next_player], main_deck, stock_deck, table)

                    else:
                        print("The Card can't be played")
                        clear_console()
                        raise TypeError
            
            if len(players[ct_turn].cards) == 1:
                refill_deck(main_deck, stock_deck, players)
                say_uno(players[ct_turn], main_deck)

            #Cheking if current player has reach 500 points
            if players[ct_turn].get_score() >= 500:
                clear_console() # Clear screen
                print("{} won with {} points".format(players[ct_turn].get_name(), players[ct_turn].get_score()))
                print('......GAME OVER......')
                sys.exit()

            # Changing turn
            ct_turn = next_player

            input('\n Press any key to continue the game...')
            clear_console() # Clear screen
    
        except ValueError:
            clear_console()
            print('Strings are not allowed, please enter an integer between 1 and', len(players[ct_turn].cards))

        except TypeError:
            clear_console()
            print("Entry out of range or you chose card that can't be played")
""" END THE GAME """