class Player:

    # Constructor
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.score = 0

    # Add point to score
    def add_points(self, amount):
        self.score += amount

    # Return player name
    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    # Show player hand
    def show_hand(self):
        count = 1
        for card in self.cards:
            print("{}: {}".format(count, card.show()))
            count += 1