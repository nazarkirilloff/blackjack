class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print ("{} of {}".format(self.value, self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
        for suit in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
            for value in [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']:
                self.cards.append(Card(suit, value))

class Player:
    pass

class Game:
    pass

card1 = Card('Spades', 'King')
card1.show()
