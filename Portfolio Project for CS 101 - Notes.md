# Portfolio Project: CS 101

### Project Parameters
The **goal** of this project is to build a basic terminal program for my friends and family to play with. After I've finished building the program, I will blog about it on my medium of choice. Below are the main project objectives

- Build a terminal program using Python
- Add at least one interactive feature using input()
- Use Git version control
- Use the command line and file navigation
- Write a technical blog post on the project

### Project Brainstorming
I've thought up several ideas for what could be useful and fun to play with in a basic terminal program. The ideas divide into two basic categories: games and tools. The games would be the most fun to play, and probably a bit more involved than the tools, so I've decided to pick one of the games that is maybe one of the more complicated ones -- Texas Hold 'Em. 

#### Games
- Blackjack
- Texas Hold 'Em
- Roulette
  
#### Tools
- Mortgage Calculator
- Payback Period Calculator
- Simple Stock DCF Modeler
- Fortune Teller
- Quotation of the Day (mood-based)

**But after doing more work on the codebase, I realized creating an algorithm for the computer to place bets against a player would be beyond my abilities right now.** So I've pared back the project to a video poker game where there is just one player and the payouts are already defined. [This resource](https://www.casinoreports.ca/video-poker/rules/) was very helpful for determining how to structure the payouts and the hierarchy of hands.

### The Rules of Video Poker
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

Betting determines the amount of the payout for the types of hands you have. Typically, a player can bet upto 5 coins on each hand. The payout table can be found at the link in the Project Brainstorming section of this doc.

### Codebase Needs for Video Poker #TODO
Based on my limited understanding of the rules of video poker, it looks like I will need code that accomplishes the following:
- [x] A deck of 52 cards with random five-card initial draw
- [x] A hierarchy of winning combinations
- [ ] A payoff table that calculates winnings for a player given their bet and their hand (based on the payoff table described and linked above)
- [x] A betting function for the player to wager a given number of coins (using the `input()` function in python)
- [ ] A method for tallying the player's current winnings/bankroll
- [x] Extra: a visual representation of the cards in the player's hand 

### Building a Deck of Cards with OO Python
I found this [really nifty blog post](https://medium.com/@anthonytapias/build-a-deck-of-cards-with-oo-python-c41913a744d3) on creating a deck of cards using three classes in Python. I used this methodology to build out the deck of cards for my Video Poker game. 

[This exchange](https://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards) was very helpful in thinking about how to build and display the graphical representations of the cards.


### Ideas
- [x] Need to find some way to sort the hand a player is dealt by card.rank
- [ ] Need to create a while loop (while player.bankroll > 0, play continues)
- [ ] Need to add functionality that asks player if they want to continue playing, OR keep the number of rounds of play at some palatable number (like 10) 