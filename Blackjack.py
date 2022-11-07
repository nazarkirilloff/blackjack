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

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.hand = []

    def draw(self):
        self.hand.append(deck.draw())
        return self

    def show_hand(self):
        for card in self.hand:
            print(card)
        print(f'{self.name} has {self.count()} points')
        print('/////////')

    def dealer_card(self):
        print(self.hand[0])
        print('''The second dealer's card is hidden until all players will decide to stand or busted''')
        print('/////////')

    def count(self):
        count = 0
        aces = 0
        for card in self.hand:
            if card[0:2] == 'Ja' or card[0:2] == 'Qu' or card[0:2] == 'Ki':
                count += 10
            elif card[0:2] == 'Ac':
                count += 11
                aces += 1
            else:
                count += int(card[0:2])

        for i in range(aces):
            if count > 21:
                count -= 10

        return count

    def bet(self, bet):
        self.money -= bet

class Game:

    def __init__(self):
        deck = Deck()
        dealer = Player('Dealer', 0)
        player_name = input('Hi! Welcome to the casino "Monte Palace"! We are happy you joined \n '
                            'our famous Blackjack table. Please type your name \n'
                            '/////////')
        player_money = input(f'Great, {player_name}! Please tell us what amount of chips do you want to buy? \n'
                             '/////////')
        player1 = Player(player_name, player_money)

        dealer.draw()
        player1.draw()
        dealer.draw()
        player1.draw()
        dealer.dealer_card()
        player1.show_hand()

    def play_again(self):
        dealer.draw()
        player1.draw()
        dealer.draw()
        player1.draw()
        dealer.dealer_card()
        player1.show_hand()

    def hit(self, player):
        player.draw()


deck = Deck()

dealer = Player('Dealer', 0)
dealer.draw()
dealer.draw()
dealer.dealer_card()

player1 = Player('Nazar', 100)
player1.draw()
player1.draw()
player1.show_hand()

dealer.show_hand()

