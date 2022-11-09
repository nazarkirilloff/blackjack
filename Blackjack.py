from random import shuffle

class Deck:

    def __init__(self):
        self.deck_to_play = []
        self.build_deck()

    def build_deck(self):
        self.deck_to_play = [f'{value} of {suit}' for suit in ['Spades', 'Clubs', 'Diamonds', 'Hearts'] for value in
                             [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']]
        shuffle(self.deck_to_play)

    def show(self):
        print(self.deck_to_play)

    def draw(self):
        return self.deck_to_play.pop(0)


class Player:

    def __init__(self, name, money):
        self.bet = None
        self.insurance_bet = 0
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

    def make_bet(self, bet):
        self.bet = bet
        self.money -= bet

class Game:

    def __init__(self):

        first_bet = int(
            input(f'''Let's get started! Please make your bet. Currently you have {player1.money} chips. \n'''
                  '>>>>> '))
        while type(first_bet) != int or first_bet > player1.money:
            first_bet = int(
                input(f'''Let's get started! Please make your bet. Currently you have {player1.money} chips. \n'''
                      '>>>>> '))
        player1.make_bet(first_bet)

        dealer.draw()
        player1.draw()
        dealer.draw()
        player1.draw()
        dealer.dealer_card()
        player1.show_hand()

        if dealer.hand[0][0:2] == 'Ac':
            if player1.money != 0:
                self.insurance()
            else:
                print("Unfortunately your don't have sufficient funds to make an insurance bet,\n"
                      "so you will have to continue playing with your bet\n"
                      "/////////")

        self.continue_round()

    def hit(self, player):
        player.draw()
        player.show_hand()
        self.check()

    def stand(self):
        self.dealer_play()

    def double(self):
        player1.money -= player1.bet
        palyer1.draw()
        self.check()
        self.stand()

    def insurance(self):
        print('The open dealer card is Ace. Do you want to make an insurance bet? If yes, type down "yes" or "y".')
        answer = input('>>>>> ')
        if answer in ['Yes', 'yes', 'y', 'Y']:
            insurance_bet = None
            while type(insurance_bet) != int and insurance_bet < player1.money:
                insurance_bet = input(
                    f'''Let's get started! Please make your insurance bet. Currently you have {player1.money} chips. \n'''
                    '>>>>> ')
            player1.bet(insurance_bet)
        else:
            print('Unfortunately you do not have any sufficient')

    def dealer_play(self):
        while dealer.count() < 16:
            dealer.draw()
        self.end_of_round()

    def play_again(self):
        player1.hand = []
        player1.insurance_bet = 0
        dealer.hand = []

        deck.build_deck()

        new_bet = int(input(f'''Let's get started! Please make your bet. Currently you have {player1.money} chips. \n'''
                            '>>>>> '))
        while type(new_bet) != int or new_bet > player1.money:
            new_bet = int(
                input(f'''Let's get started! Please make your bet. Currently you have {player1.money} chips. \n'''
                      '>>>>> '))
        player1.make_bet(new_bet)

        dealer.draw()
        player1.draw()
        dealer.draw()
        player1.draw()
        dealer.dealer_card()
        player1.show_hand()

        if dealer.hand[0][0:2] == 'Ac':
            if player1.money != 0:
                self.insurance()
            else:
                print("Unfortunately your don't have sufficient funds to make an insurance bet,\n"
                      "so you will have to continue playing with your bet\n"
                      "/////////")

        self.continue_round()

    def check(self):
        if player1.count() >= 21:
            self.end_of_round()
        self.continue_round()

    def continue_round(self):
        continue_round = None
        while continue_round not in ['Hit', 'hit', 'Stand', 'stand', 'Double', 'double']:
            continue_round = str(input('Please, type down your next move (hit, stand or double) \n'
                                       '>>>>> '))

        if continue_round.lower() == 'hit':
            self.hit(player1)
        elif continue_round.lower() == 'stand':
            self.stand()
        else:
            self.double()

    # Check every possible ending of the round.
    def end_of_round(self):
        dealer.show_hand()
        player1.show_hand()

        if player1.insurance_bet > 0:
            if dealer.count() == 21:
                print('The dealer has a blackjack and your insurance bet won.\n'
                      '/////////')
                player1.money += 2 * player1.insurance_bet
            else:
                print("The dealer didn't have a blackjack, you lost your insurance bet.\n"
                      "/////////")

        if player1.count() == 21 and dealer.count() != 21:
            player1.money += 2.5 * player1.bet
            print('Woohoo, you got 21 points! You win 3 to 2 for your Blackjack. \n'
                  'You are on fire! \n'
                  '/////////')
        elif dealer.count() > 21 >= player1.count():
            player1.money += 2 * player1.bet
            print('It seems the dealer got busted! You win and get double your bet back. \n'
                  'Good luck in the next round! \n'
                  '/////////')
        elif player1.count() > 21:
            print('Unfortunately you got busted. You lose your bet. \n'
                  'Good luck in the next round! \n'
                  '/////////')
        elif player1.count() == dealer.count():
            player1.money += player1.bet
            print('Ooh, so close! Unfortunately, it is a push. Both you and the dealer got same points. \n'
                  'You get your bet back and good luck in the next round! \n'
                  '/////////')
        elif player1.count() > dealer.count():
            player1.money += 2 * player1.bet
            print('You won and get the 2 times your bet back. Congratulations!\n'
                  '/////////')
        else:
            print('Unfortunately you lost. You bet goes to casino. \n'
                  'Good luck in the next round! \n'
                  '/////////')

        if player1.money > 0:
            decision = input('Do you want to continue the game? Print "yes" to continue.\n'
                             '>>>>> ')
            if decision in ['yes', 'Yes', 'yess', 'Yess']:
                self.play_again()
            else:
                print(f'We are sorry to see you go {player1.name})-:\n'
                      'Anyway thank you for visiting "Monte Palace" casino.\n'
                      'We hope to see you again soon!')

        if player1.money == 0:
            print("It seems that unfortunately you don't have more chips to play.\n"
                  'We will gladly see on your next visit to "Monte Palace" casino!')


# The first things needed to start the game.
deck = Deck()

dealer = Player('Dealer', 0)

player_name = input('Hi! Welcome to the casino "Monte Palace"! We are happy you joined \n'
                    'our famous Blackjack table. We have a common rule "Blackjack wins 3 to 2". \n'
                    'We offer options to stand, hit or double while playing. \n'
                    'Please type your name down below.\n'
                    '>>>>> ')

player_money = int(input(f'Great, {player_name}! Please tell us what amount of chips do you want to buy? \n'
                         '>>>>> '))

while type(player_money) != int or player_money < 0:
    player_money = int(input(f'Great, {player_name}! Please tell us what amount of chips do you want to buy? \n'
                             '>>>>> '))

player1 = Player(player_name, player_money)

game = Game()
