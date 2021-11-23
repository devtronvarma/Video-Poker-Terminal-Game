# Video Poker in the Terminal: a Python-based Video Poker Game

## Intro

### Why I Built This
Sometimes we need to take a break from our hectic lives and play something just for fun. I built myself a little video poker game that runs in the terminal based on coding practices I've picked up online. Building this game was a way for me to practice building objects in Python, creating loops, and learning a bit about fun packages that are available for displaying text in the terminal (I'm looking at you pyfiglet).

### What is Video Poker?
 Video poker is based on the classic 5-card draw of table poker. A player starts by hitting the deal button, placing a bet, and getting an initial hand of 5 cards. The player then has the option to be redealt certain cards to collect a winning combination. The hands are ranked in the following order: 

* Royal Flush
* Straight Flush
* Four of a Kind
* Full House
* Flush
* Straight
* Three of a Kind
* Two Pair
* Jacks or Better

Betting determines the amount of the payout for the types of hands you have. Typically, a player can bet upto 5 coins on each hand. I used some of the rules of video poker I found [online](https://www.casinoreports.ca/video-poker/rules/) as a guideline for the multipliers I used in my version of the game.
 
 The game is a pure randomness machine combined with some elements of skill and probability. The more one knows about the probabilities of getting certain winning hands, the better their odds of increasing their bankroll.

## Basic Building Blocks of the Game
Based on my limited understanding of the rules of video poker, I figured I would need the following:

### A Deck of Cards
I built a Deck class that was based on another class of cards (called the Card class in my code). The card class simply defines the suit, rank, and number of points for a given card, and I am grateful for the code shared [here](https://medium.com/@anthonytapias/build-a-deck-of-cards-with-oo-python-c41913a744d3) to help me build my own Deck class. The suit and rank are then used in the card display function I created to display an ascii version of the card (more on that later), while the points are used later (in conjunction with the suit) to determine scoring for the player's hand. The Deck class initializes to build a deck of 52 cards (just like the ones used in table poker), and I included methods for displaying the cards in the deck, shuffling the deck, and then drawing a card from the deck. 

### A Player with Appropriate Actions
The next big set of functionality had to do with what a player could do. When the Player class is initiated, there's an initial bankroll to bet from of 20 coins. I gave the player the ability to draw an initial hand of 5 cards, which relies on the draw_card method available to the Deck class. I also built core methods for betting, redrawing, and scoring the player's hand to output both the category of winning hand the player has and what her updated bankroll is with the winnings. 

### A Loop for Gameplay
In order to set the game going and have it going until either (a) the player ran out of coins or (b) decided to go do something else (like get back to work), I realized I would need to build the game flow as a while loop with logic switches for conditions (a) and (b). Once I had this settled, I added a few extra visual items and did some refactoring to give the game a little more visual appeal.

Using the `input()` function in python was helpful for creating the prompts needed to get the player's bet as well as determine if they still wanted to play. 

### Displaying the Cards and Welcome Message
[This exchange](https://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards) proved very helpful in creating a way to display the cards in the player's hand in a more appealing. Adding to that, I found a library called [pyfiglet](https://github.com/pwaller/pyfiglet) that spruced up the look of the game upon first starting it.  


## Demo of Gameplay
