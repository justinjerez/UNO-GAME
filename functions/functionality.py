import time
import sys

from classes.card import *
from classes.player import *
from functions.abstracts import *

def next_turn(players, current_turn, game_direction, last_card_played):
    nums_of_players = len(players)

    if game_direction is True:
        if last_card_played.value is 'pass':
            if current_turn is nums_of_players - 2:
                next_turn = 0
            elif current_turn is nums_of_players - 1:
                next_turn = 1
            else:
                next_turn = current_turn + 2
        elif last_card_played.value is 'reverse':
            game_direction = False
            if current_turn is 0:
                next_turn = nums_of_players - 1
            else:
                next_turn = current_turn - 1
        else:
            if current_turn is nums_of_players - 1:
                next_turn = 0
            else:
                next_turn = current_turn + 1
    else:
        if last_card_played.value is 'pass':
            if current_turn is 0:
                next_turn = nums_of_players - 2
            elif current_turn is 1:
                next_turn = nums_of_players - 1
            else:
                next_turn = current_turn - 2
        elif last_card_played.value is 'reverse':
            game_direction = True
            if current_turn is nums_of_players - 1:
                next_turn = 0
            else: 
                next_turn = current_turn + 1
        else:
            if current_turn is 0:
                next_turn = nums_of_players - 1
            else:
                next_turn = current_turn - 1
    
    return [next_turn, game_direction]

# Carry out actions of a action card
def carry_out_action(current_player, next_player, deck, stock, table):
    if stock.cards[-1].suit == 'Wilds':
        #Changing table color without any value
        table = Card('None', select_color())

        # Adds four card to next player and change color of the table
        if stock.cards[-1].value == '+4':
            current_player.add_points(50)
            for i in range(0, 4):
                move_card(deck, next_player, -1)
        else:
            current_player.add_points(50)

    else:
        #Changing table to the last card in stock
        table = stock.cards[-1]

        # Adds two card to next player
        if stock.cards[-1].value == '+2':
            current_player.add_points(20)
            for i in range(0, 2):
                move_card(deck, next_player, -1)

        elif stock.cards[-1].value == 'pass':
            current_player.add_points(20)

        elif stock.cards[-1].value == 'reverse':
            current_player.add_points(20)
    
    return table

# Gives to all players 7 cards
def hand_out_cards(players, deck):
    for player in players:
        count = 0
        while count < 7:
            player.cards.append(deck.cards.pop())
            count += 1

# Determine if a card is a playable card
def is_playable(player_card, table_card):
    if player_card.suit is 'Wilds':
        return True
    else:
        if player_card.suit is table_card.suit or player_card.value is table_card.value:
            return True
        
    return False

# Refill a deck
def refill_deck(filling, emptying, players):
    if len(filling.cards) <= 4:
        if len(emptying.cards) >= 4:
            for card in emptying.cards:
                filling.cards.append(card)
                filling.shuffle()
            emptying.clear()
        else:
            count = 1
            winner = 0
            while(count < len(players)):
                if players[count].get_score() > players[count - 1].get_score():
                    winner = count
                else:
                    winner = count - 1
            print('\nRan out of cards')
            print("{} won with {} points".format(players[winner].get_name(), players[winner].get_score()))
            print('......GAME OVER......')
            sys.exit()
    

# Moves a card from point a to point b
def move_card(sender, receiver, card_position):
    receiver.cards.append(sender.cards.pop(card_position))

def say_uno(player, deck):
    print('You have only one card, say UNO!. PRESS CRTL + C')
    counter = 3

    while True:
        try:
            print(counter)
            counter -= 1
            time.sleep(1)

            if counter == 0:
                clear_console()
                print('You did not say UNO, take two cards')
                for i in range(0, 2):
                    move_card(deck, player, -1)
                input("\nPress enter to continue...")
                clear_console()
                break

        except KeyboardInterrupt:
            clear_console()
            print("{} wins".format(player.get_name()))
            print('......GAME OVER......')
            input("\nPress enter to continue...")
            clear_console()
            sys.exit()

#  When a suit of a played card is specials, you can select a color to the next play
def select_color():
    suits = ['Blues', 'Greens', 'Reds', 'Yellows']

    while(True):
        try:
            print("\n1. Blues")
            print("2. Greens")
            print("3. Reds")
            print("4. Yellows\n")

            opt = int(input("Select a number from above: "))

            if opt < 1 or opt > 4:
                raise TypeError
            else:
                return suits[opt - 1];

            clear_console()
            break

        except ValueError:
            clear_console()
            print('Strings are not allowed, please enter an integer between 1 and 4')

        except TypeError:
            clear_console()
            print('Entry out of range, please enter a number from below')