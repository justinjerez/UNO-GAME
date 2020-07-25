class Player:

    # Constructor
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.score = 0

    # Return player name
    def get_name(self):
        return self.name