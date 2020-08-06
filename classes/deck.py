import random

from .card import Card


class Deck(object):

    # Constructor
    def __init__(self):
        self.cards = []
        self.fill()
        self.shuffle()

    # Clear Deck
    def clear(self):
        del self.cards[:]


    # Fill Deck
    def fill(self):
        # Create cards by suit
        for suit in ['Greens', 'Blues', 'Yellows', 'Reds', 'Wilds']:
            if suit == 'Wilds':
                for value in ['+4', 'Change Color']:
                    count = 0
                    while count < 4:
                        self.cards.append(Card(value, suit))
                        count += 1
            else:
                for value in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '+2', 'reverse', 'pass']:
                    n = 2
                    count = 0

                    if value is 0:
                        n = 1

                    while count < n:
                        self.cards.append(Card(value, suit))
                        count += 1

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i);
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
