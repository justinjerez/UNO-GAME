import time

from functions.abstracts import *

# Refill a deck
def refill_deck(filling, emptying):
    for card in emptying.cards:
        filling.cards.append(card)
        filling.shuffle()
    emptying.clear()

# Gives to all players 7 cards
def hand_out_cards(players, deck):
    for player in players:
        count = 0
        while count < 7:
            player.cards.append(deck.cards.pop())
            count += 1

# Moves a card from point a to point b
def move_card(sender, receiver, card_position):
    receiver.cards.append(sender.cards.pop(card_position))

def say_uno(player_name):
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
                take_cards(players[T], deck, 3)
                input("\nPress enter to continue...")
                clear_console()
                break

        except KeyboardInterrupt:
            clear_console()
            print("{} wins".format(player_name))
            print('GAME OVER')
            input("\nPress enter to continue...")
            clear_console()
            sys.exit()

def is_playable(player_card, table_card):
    if player_card.suit is 'Wilds':
        return True
    else:
        if player_card.suit is table_card.suit or player_card.value is table_card.value:
            return True
        
    return False
    