def hand_out_cards(players, deck):
    for player in players:
        count = 0
        while count < 7:
            player.cards.append(deck.cards.pop())
            count += 1