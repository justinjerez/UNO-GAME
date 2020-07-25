class Card:
    
    # Constructor
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    # Return card
    def show(self):
        return '{} of {}'.format(self.value, self.suit)