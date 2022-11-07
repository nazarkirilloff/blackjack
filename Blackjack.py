from random import shuffle

class Deck:

    def __init__(self):
        self.deck_to_play = []
        self.build_deck()

    def build_deck(self):
        self.deck_to_play = [f'{value} of {suit}' for suit in ['Spades', 'Clubs', 'Diamonds', 'Hearts'] for value in [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']]
        shuffle(self.deck_to_play)

    def show(self):
        print(self.deck_to_play)

    def draw(self):
        return self.deck_to_play.pop(0)

class Player:
    pass

class Game:
    pass

deck = Deck()
deck.show()

dealer = Player()
