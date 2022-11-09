# blackjack

BLACKJACK Project
Lets you play text-based blackjack for 1 player vs casino.

Realized Classes:
Deck (52 Cards, Random Shuffle, Draw)
Player (Dealer, Player, Money to play)
Game (Start, Win, Lose, Point Count)

How it works:
At the beginning of the game player(s) will provide the name
and amount of money they want to play with.
Player(s) can start the game and play via the input function
in the terminal.
It will let make bets by player.
It will let to decide if player wants one more card or stop.
It will be saving the point results of each participant.
It will be able to finish the game and determine the winner.
If the winner is casino player's bet is gone.
If the winner is player - he will get the winning bet to his account.
Each player will see his total points and cards everyone
else have when choosing to draw or not and after the draw.
When the game is over either by player's win or lose, player will
be offered to play again, unless his total money is 0.

Important Rules taken into consideration while developing:

1) Dealer will draw by two cards at the beginning of the game:
- By 1 to everyone open.
- Second hidden for himself and open for every other player.

2) Ace can be 1 or 11, depending on which is more profitable:
- 11 (soft) if the sum with other cards gives 21 or less.
- 1 (hard) if the sum of 11 with other cards gives more than 21.

3) Chance for Insurance bet if dealer has Ace as an open card.
If opened card will give the Blackjack, player will get his 2x
Insurance bet, but still loses the initial one if he don't also
have a Blackjack.

4) 2 to 10 gives points according to its face value.
Jack, Queen and King give 10 points.

5) If player got Blackjack he wins 2.5x bet, if Dealer doesn't
also have Blackjack 

6) If player wins vs Dealer not with Blackjack or Dealer got
>21 points, he wins 2x bet.

7) Bets are placed by the player before cards are given.

8) Player have a choice to Hit (get one more card), Stand (stay
with the dealt before cards), Double (double his bet and get only
ONE more card), Insurance (point #3)

9) The dealer is required to play his hand after all players stand
on their hands. After revealing the second card, dealer must
continue to draw cards if his total is 16 or less. If the total
is 17 or more - dealer stops drawing cards.

10) Player win vs Dealer if Dealer got bust (>21 points) or his
total points is higher than the Dealer's. In case of Push (tie)
Player just take his bet back.

11) If player got bust, dealer did not play his hand and player
loses his bet.
